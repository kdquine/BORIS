# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_modifier.ui'
#
# Created: Fri Jul  7 12:43:56 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(638, 510)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbModifier = QtGui.QLabel(Dialog)
        self.lbModifier.setObjectName(_fromUtf8("lbModifier"))
        self.verticalLayout_2.addWidget(self.lbModifier)
        self.leModifier = QtGui.QLineEdit(Dialog)
        self.leModifier.setObjectName(_fromUtf8("leModifier"))
        self.verticalLayout_2.addWidget(self.leModifier)
        self.lbCode = QtGui.QLabel(Dialog)
        self.lbCode.setObjectName(_fromUtf8("lbCode"))
        self.verticalLayout_2.addWidget(self.lbCode)
        self.leCode = QtGui.QLineEdit(Dialog)
        self.leCode.setObjectName(_fromUtf8("leCode"))
        self.verticalLayout_2.addWidget(self.leCode)
        self.lbCodeHelp = QtGui.QLabel(Dialog)
        self.lbCodeHelp.setWordWrap(True)
        self.lbCodeHelp.setObjectName(_fromUtf8("lbCodeHelp"))
        self.verticalLayout_2.addWidget(self.lbCodeHelp)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pbAddModifier = QtGui.QPushButton(Dialog)
        self.pbAddModifier.setText(_fromUtf8(""))
        self.pbAddModifier.setObjectName(_fromUtf8("pbAddModifier"))
        self.verticalLayout_3.addWidget(self.pbAddModifier)
        self.pbModifyModifier = QtGui.QPushButton(Dialog)
        self.pbModifyModifier.setText(_fromUtf8(""))
        self.pbModifyModifier.setObjectName(_fromUtf8("pbModifyModifier"))
        self.verticalLayout_3.addWidget(self.pbModifyModifier)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidgetModifiersSets = QtGui.QTabWidget(Dialog)
        self.tabWidgetModifiersSets.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tabWidgetModifiersSets.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidgetModifiersSets.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidgetModifiersSets.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidgetModifiersSets.setDocumentMode(True)
        self.tabWidgetModifiersSets.setObjectName(_fromUtf8("tabWidgetModifiersSets"))
        self.verticalLayout.addWidget(self.tabWidgetModifiersSets)
        self.lbSetName = QtGui.QLabel(Dialog)
        self.lbSetName.setObjectName(_fromUtf8("lbSetName"))
        self.verticalLayout.addWidget(self.lbSetName)
        self.leSetName = QtGui.QLineEdit(Dialog)
        self.leSetName.setObjectName(_fromUtf8("leSetName"))
        self.verticalLayout.addWidget(self.leSetName)
        self.lbType = QtGui.QLabel(Dialog)
        self.lbType.setObjectName(_fromUtf8("lbType"))
        self.verticalLayout.addWidget(self.lbType)
        self.cbType = QtGui.QComboBox(Dialog)
        self.cbType.setObjectName(_fromUtf8("cbType"))
        self.cbType.addItem(_fromUtf8(""))
        self.cbType.addItem(_fromUtf8(""))
        self.cbType.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.cbType)
        self.lbValues = QtGui.QLabel(Dialog)
        self.lbValues.setObjectName(_fromUtf8("lbValues"))
        self.verticalLayout.addWidget(self.lbValues)
        self.lwModifiers = QtGui.QListWidget(Dialog)
        self.lwModifiers.setObjectName(_fromUtf8("lwModifiers"))
        self.verticalLayout.addWidget(self.lwModifiers)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbMoveUp = QtGui.QPushButton(Dialog)
        self.pbMoveUp.setObjectName(_fromUtf8("pbMoveUp"))
        self.horizontalLayout.addWidget(self.pbMoveUp)
        self.pbMoveDown = QtGui.QPushButton(Dialog)
        self.pbMoveDown.setObjectName(_fromUtf8("pbMoveDown"))
        self.horizontalLayout.addWidget(self.pbMoveDown)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pbRemoveModifier = QtGui.QPushButton(Dialog)
        self.pbRemoveModifier.setObjectName(_fromUtf8("pbRemoveModifier"))
        self.verticalLayout.addWidget(self.pbRemoveModifier)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbAddSet = QtGui.QPushButton(Dialog)
        self.pbAddSet.setObjectName(_fromUtf8("pbAddSet"))
        self.horizontalLayout_3.addWidget(self.pbAddSet)
        self.pbRemoveSet = QtGui.QPushButton(Dialog)
        self.pbRemoveSet.setObjectName(_fromUtf8("pbRemoveSet"))
        self.horizontalLayout_3.addWidget(self.pbRemoveSet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbMoveSetLeft = QtGui.QPushButton(Dialog)
        self.pbMoveSetLeft.setObjectName(_fromUtf8("pbMoveSetLeft"))
        self.horizontalLayout_4.addWidget(self.pbMoveSetLeft)
        self.pbMoveSetRight = QtGui.QPushButton(Dialog)
        self.pbMoveSetRight.setObjectName(_fromUtf8("pbMoveSetRight"))
        self.horizontalLayout_4.addWidget(self.pbMoveSetRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pbCancel = QtGui.QPushButton(Dialog)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(Dialog)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.tabWidgetModifiersSets.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Set modifiers", None))
        self.lbModifier.setText(_translate("Dialog", "Modifier", None))
        self.lbCode.setText(_translate("Dialog", "Key code", None))
        self.lbCodeHelp.setText(_translate("Dialog", "Key code is case insensitive. Type one character or a function key (F1, F2... F12)", None))
        self.lbSetName.setText(_translate("Dialog", "Set name", None))
        self.lbType.setText(_translate("Dialog", "Modifier type", None))
        self.cbType.setItemText(0, _translate("Dialog", "Single selection", None))
        self.cbType.setItemText(1, _translate("Dialog", "Multiple selection", None))
        self.cbType.setItemText(2, _translate("Dialog", "Numeric", None))
        self.lbValues.setText(_translate("Dialog", "Values", None))
        self.pbMoveUp.setText(_translate("Dialog", "Move modifier up", None))
        self.pbMoveDown.setText(_translate("Dialog", "Move modifier down", None))
        self.pbRemoveModifier.setText(_translate("Dialog", "Remove modifier", None))
        self.pbAddSet.setText(_translate("Dialog", "Add set of modifiers", None))
        self.pbRemoveSet.setText(_translate("Dialog", "Remove set of modifiers", None))
        self.pbMoveSetLeft.setText(_translate("Dialog", "Move set left", None))
        self.pbMoveSetRight.setText(_translate("Dialog", "Move set right", None))
        self.pbCancel.setText(_translate("Dialog", "Cancel", None))
        self.pbOK.setText(_translate("Dialog", "OK", None))

