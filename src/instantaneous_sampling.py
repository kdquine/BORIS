"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2019 Olivier Friard

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
"""

import os
import pathlib
import re
import time

from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox

import dialog
import project_functions
import select_observations
import tablib
import utilities
from config import *


def instantaneous_sampling_analysis(pj: dict,
                                    selected_observations: list,
                                    parameters_obs: dict,
                                    time_interval: float) -> dict:
    """
    Instantaneous samplig analysis

    Args:
        pj (dict): project dictionary
        selected_observations (list): list of selected observations
        parameters_obs (dict): dcit of parameters
        time_interval (float): time interval (in seconds)

    Returns:
        dict: dictionary of tablib dataset

    """

    results_df = {}

    state_behavior_codes = [x for x in utilities.state_behavior_codes(pj[ETHOGRAM]) if x in parameters_obs[SELECTED_BEHAVIORS]]

    for obs_id in selected_observations:

        if obs_id not in results_df:
            results_df[obs_id] = {}

        for subject in parameters_obs[SELECTED_SUBJECTS]:

            # extract tuple (behavior, modifier)
            behav_modif_list = [(idx[2], idx[3])
                                for idx in pj[OBSERVATIONS][obs_id][EVENTS] if idx[1] == (subject if subject != NO_FOCAL_SUBJECT else "")]

            # extract observed subjects NOT USED at the moment
            observed_subjects = [event[1] for event in pj[OBSERVATIONS][obs_id][EVENTS]]

            # add selected behavior if not found in (behavior, modifier)
            if not parameters_obs[EXCLUDE_BEHAVIORS]:
                for behav in parameters_obs[SELECTED_BEHAVIORS]:
                    if behav not in [x[0] for x in behav_modif_list]:
                        behav_modif_list.append((behav, ""))

            behav_modif_set = set(behav_modif_list)

            if parameters_obs[INCLUDE_MODIFIERS]:
                results_df[obs_id][subject] = tablib.Dataset(headers=["time"] + [f"{x[0]}" + f" ({x[1]})" * (x[1] != "")
                                                                                 for x in sorted(behav_modif_set)])
            else:
                results_df[obs_id][subject] = tablib.Dataset(headers=["time"] + [x[0] for x in sorted(behav_modif_set)])

            if subject == NO_FOCAL_SUBJECT:
                sel_subject_dict = {"": {SUBJECT_NAME: ""}}
            else:
                sel_subject_dict = dict([(idx, pj[SUBJECTS][idx]) for idx in pj[SUBJECTS] if pj[SUBJECTS][idx][SUBJECT_NAME] == subject])

            row_idx = 0
            t = parameters_obs[START_TIME]
            while t < parameters_obs[END_TIME]:

                current_states = utilities.get_current_states_modifiers_by_subject(state_behavior_codes,
                                                                                   pj[OBSERVATIONS][obs_id][EVENTS],
                                                                                   sel_subject_dict,
                                                                                   t,
                                                                                   include_modifiers=parameters_obs[INCLUDE_MODIFIERS])

                cols = [float(t)]  # time

                for behav in results_df[obs_id][subject].headers[1:]:  # skip time
                    cols.append(int(behav in current_states[list(current_states.keys())[0]]))

                results_df[obs_id][subject].append(cols)

                t += time_interval
                row_idx += 1

    return results_df


def instantaneous_sampling(pj: dict):


    result, selected_observations = select_observations.select_observations(pj,
                                                                            MULTIPLE,
                                                                            "Select observations for instantaneous sampling")

    if not selected_observations:
        return
    # check if state events are paired
    out = ""
    not_paired_obs_list = []
    for obs_id in selected_observations:
        r, msg = project_functions.check_state_events_obs(obs_id, pj[ETHOGRAM],
                                                          pj[OBSERVATIONS][obs_id])

        if not r:
            out += f"Observation: <strong>{obs_id}</strong><br>{msg}<br>"
            not_paired_obs_list.append(obs_id)

    if out:
        out = f"The observations with UNPAIRED state events will be removed from tha analysis<br><br>{out}"
        results = dialog.Results_dialog()
        results.setWindowTitle(f"{programName} - Check selected observations")
        results.ptText.setReadOnly(True)
        results.ptText.appendHtml(out)
        results.pbSave.setVisible(False)
        results.pbCancel.setVisible(True)

        if not results.exec_():
            return
    selected_observations = [x for x in selected_observations if x not in not_paired_obs_list]
    if not selected_observations:
        return

    max_obs_length, selectedObsTotalMediaLength = project_functions.observation_length(pj, selected_observations)
    if max_obs_length == -1:  # media length not available, user choose to not use events
        return

    parameters = dialog.choose_obs_subj_behav_category(pj,
                                                       selected_observations,
                                                       maxTime=max_obs_length,
                                                       flagShowExcludeBehaviorsWoEvents=True,
                                                       by_category=False)

    if not parameters[SELECTED_SUBJECTS] or not parameters[SELECTED_BEHAVIORS]:
        QMessageBox.warning(None, programName, "Select subject(s) and behavior(s) to analyze")
        return

    # ask for time interval
    i, ok = QInputDialog.getDouble(None, "Instantaneous sampling", "Time interval (in seconds):", 1.0, 0.001, 86400, 3)
    if not ok:
        return
    time_interval = utilities.float2decimal(i)

    # self.statusbar.showMessage("Instantaneous sampling is running. Please wait...", 0)
    # app.processEvents()

    results_df = instantaneous_sampling_analysis(pj,
                                                 selected_observations,
                                                 parameters,
                                                 time_interval)

    # self.statusbar.showMessage("Instantaneous sampling done...", 5000)
    # app.processEvents()

    # save results
    if len(selected_observations) == 1:
        extended_file_formats = ["Tab Separated Values (*.tsv)",
                                 "Comma Separated Values (*.csv)",
                                 "Open Document Spreadsheet ODS (*.ods)",
                                 "Microsoft Excel Spreadsheet XLSX (*.xlsx)",
                                 "Legacy Microsoft Excel Spreadsheet XLS (*.xls)",
                                 "HTML (*.html)"]
        file_formats = ["tsv",
                        "csv",
                        "ods",
                        "xlsx",
                        "xls",
                        "html"]

        file_name, filter_ = QFileDialog().getSaveFileName(None, "Save results", "", ";;".join(extended_file_formats))
        if not file_name:
            return

        output_format = file_formats[extended_file_formats.index(filter_)]

        if pathlib.Path(file_name).suffix != "." + output_format:
            file_name = str(pathlib.Path(file_name)) + "." + output_format
            # check if file with new extension already exists
            if pathlib.Path(file_name).is_file():
                if dialog.MessageDialog(programName,
                                        f"The file {file_name} already exists.",
                                        [CANCEL, OVERWRITE]) == CANCEL:
                    return
    else:
        items = ("Tab Separated Values (*.tsv)",
                 "Comma separated values (*.csv)",
                 "Open Document Spreadsheet (*.ods)",
                 "Microsoft Excel Spreadsheet XLSX (*.xlsx)",
                 "Legacy Microsoft Excel Spreadsheet XLS (*.xls)",
                 "HTML (*.html)")

        item, ok = QInputDialog.getItem(None, "Save results", "Available formats", items, 0, False)
        if not ok:
            return
        output_format = re.sub(".* \(\*\.", "", item)[:-1]

        export_dir = QFileDialog().getExistingDirectory(None, "Choose a directory to save results",
                                                        os.path.expanduser("~"),
                                                        options=QFileDialog.ShowDirsOnly)
        if not export_dir:
            return

    mem_command = ""
    for obs_id in results_df:

        for subject in results_df[obs_id]:

            if len(selected_observations) > 1:
                file_name_with_subject = str(pathlib.Path(pathlib.Path(export_dir)
                                             / utilities.safeFileName(obs_id + "_" + subject)).with_suffix("." + output_format))
            else:
                file_name_with_subject = str(pathlib.Path(os.path.splitext(file_name)[0]
                                             + utilities.safeFileName("_" + subject)).with_suffix("." + output_format))

            # check if file with new extension already exists
            if mem_command != OVERWRITE_ALL and pathlib.Path(file_name_with_subject).is_file():
                if mem_command == "Skip all":
                    continue
                mem_command = dialog.MessageDialog(programName,
                                                   f"The file {file_name_with_subject} already exists.",
                                                   [OVERWRITE, OVERWRITE_ALL, "Skip", "Skip all", CANCEL])
                if mem_command == CANCEL:
                    return
                if mem_command == "Skip":
                    continue

            try:
                if output_format in ["csv", "tsv", "html"]:
                    with open(file_name_with_subject, "wb") as f:
                        f.write(str.encode(results_df[obs_id][subject].export(output_format)))

                if output_format in ["ods", "xlsx", "xls"]:
                    with open(file_name_with_subject, "wb") as f:
                        f.write(results_df[obs_id][subject].export(output_format))

            except Exception:

                error_type, error_file_name, error_lineno = utilities.error_info(sys.exc_info())
                logging.critical(f"Error in instantaneous sampling function: {error_type} {error_file_name} {error_lineno}")

                QMessageBox.critical(None, programName, f"Error saving file: {error_type}")
                return
