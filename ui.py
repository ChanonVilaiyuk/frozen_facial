# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'O:\studioTools\maya\python\tool\rig\facialTexture\ui.ui'
#
# Created: Tue Oct 27 18:33:13 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from qtshim import QtCore, QtGui
from qtshim import Signal
from qtshim import wrapinstance


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

class Ui_FacialRigWindow(object):
    def setupUi(self, FacialRigWindow):
        FacialRigWindow.setObjectName(_fromUtf8("FacialRigWindow"))
        FacialRigWindow.resize(476, 554)
        self.centralwidget = QtGui.QWidget(FacialRigWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.project_comboBox = QtGui.QComboBox(self.centralwidget)
        self.project_comboBox.setObjectName(_fromUtf8("project_comboBox"))
        self.gridLayout.addWidget(self.project_comboBox, 0, 1, 1, 1)
        self.type_comboBox = QtGui.QComboBox(self.centralwidget)
        self.type_comboBox.setObjectName(_fromUtf8("type_comboBox"))
        self.gridLayout.addWidget(self.type_comboBox, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.subType_comboBox = QtGui.QComboBox(self.centralwidget)
        self.subType_comboBox.setObjectName(_fromUtf8("subType_comboBox"))
        self.gridLayout.addWidget(self.subType_comboBox, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.asset_comboBox = QtGui.QComboBox(self.centralwidget)
        self.asset_comboBox.setObjectName(_fromUtf8("asset_comboBox"))
        self.gridLayout.addWidget(self.asset_comboBox, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.path_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.path_lineEdit.setText(_fromUtf8(""))
        self.path_lineEdit.setObjectName(_fromUtf8("path_lineEdit"))
        self.horizontalLayout.addWidget(self.path_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.base_comboBox = QtGui.QComboBox(self.centralwidget)
        self.base_comboBox.setObjectName(_fromUtf8("base_comboBox"))
        self.horizontalLayout_4.addWidget(self.base_comboBox)
        self.import_pushButton = QtGui.QPushButton(self.centralwidget)
        self.import_pushButton.setObjectName(_fromUtf8("import_pushButton"))
        self.horizontalLayout_4.addWidget(self.import_pushButton)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.work_listWidget = QtGui.QListWidget(self.centralwidget)
        self.work_listWidget.setObjectName(_fromUtf8("work_listWidget"))
        self.horizontalLayout_2.addWidget(self.work_listWidget)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rig_pushButton = QtGui.QPushButton(self.centralwidget)
        self.rig_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.rig_pushButton.setObjectName(_fromUtf8("rig_pushButton"))
        self.gridLayout_2.addWidget(self.rig_pushButton, 9, 0, 1, 1)
        self.clearAnim_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearAnim_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearAnim_pushButton.setObjectName(_fromUtf8("clearAnim_pushButton"))
        self.gridLayout_2.addWidget(self.clearAnim_pushButton, 11, 0, 1, 1)
        self.render_pushButton = QtGui.QPushButton(self.centralwidget)
        self.render_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.render_pushButton.setObjectName(_fromUtf8("render_pushButton"))
        self.gridLayout_2.addWidget(self.render_pushButton, 7, 0, 1, 1)
        self.open_pushButton = QtGui.QPushButton(self.centralwidget)
        self.open_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.open_pushButton.setObjectName(_fromUtf8("open_pushButton"))
        self.gridLayout_2.addWidget(self.open_pushButton, 4, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_8.addWidget(self.label_13)
        self.renderRes_comboBox = QtGui.QComboBox(self.centralwidget)
        self.renderRes_comboBox.setObjectName(_fromUtf8("renderRes_comboBox"))
        self.horizontalLayout_8.addWidget(self.renderRes_comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 5, 0, 1, 1)
        self.clearRender_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearRender_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearRender_pushButton.setObjectName(_fromUtf8("clearRender_pushButton"))
        self.gridLayout_2.addWidget(self.clearRender_pushButton, 10, 0, 1, 1)
        self.anim_pushButton = QtGui.QPushButton(self.centralwidget)
        self.anim_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.anim_pushButton.setObjectName(_fromUtf8("anim_pushButton"))
        self.gridLayout_2.addWidget(self.anim_pushButton, 8, 0, 1, 1)
        self.save_pushButton = QtGui.QPushButton(self.centralwidget)
        self.save_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.save_pushButton.setObjectName(_fromUtf8("save_pushButton"))
        self.gridLayout_2.addWidget(self.save_pushButton, 3, 0, 1, 1)
        self.clearAll_pushButton = QtGui.QPushButton(self.centralwidget)
        self.clearAll_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clearAll_pushButton.setObjectName(_fromUtf8("clearAll_pushButton"))
        self.gridLayout_2.addWidget(self.clearAll_pushButton, 12, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_9.addWidget(self.label_14)
        self.animRes_comboBox = QtGui.QComboBox(self.centralwidget)
        self.animRes_comboBox.setObjectName(_fromUtf8("animRes_comboBox"))
        self.horizontalLayout_9.addWidget(self.animRes_comboBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        self.copyTexture_pushButton = QtGui.QPushButton(self.centralwidget)
        self.copyTexture_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.copyTexture_pushButton.setObjectName(_fromUtf8("copyTexture_pushButton"))
        self.gridLayout_2.addWidget(self.copyTexture_pushButton, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        FacialRigWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FacialRigWindow)
        QtCore.QMetaObject.connectSlotsByName(FacialRigWindow)

    def retranslateUi(self, FacialRigWindow):
        FacialRigWindow.setWindowTitle(_translate("FacialRigWindow", "PT Facial Texture Rig", None))
        self.label_4.setText(_translate("FacialRigWindow", "Project", None))
        self.label_5.setText(_translate("FacialRigWindow", "Type", None))
        self.label_6.setText(_translate("FacialRigWindow", "Subtype", None))
        self.label_7.setText(_translate("FacialRigWindow", "Asset Name : ", None))
        self.label_2.setText(_translate("FacialRigWindow", "Path : ", None))
        self.label_8.setText(_translate("FacialRigWindow", "Select base : ", None))
        self.import_pushButton.setText(_translate("FacialRigWindow", "Import base", None))
        self.rig_pushButton.setText(_translate("FacialRigWindow", "Rig Controller", None))
        self.clearAnim_pushButton.setText(_translate("FacialRigWindow", "Clear Anim Nodes", None))
        self.render_pushButton.setText(_translate("FacialRigWindow", "Rig Render Face", None))
        self.open_pushButton.setText(_translate("FacialRigWindow", "Open", None))
        self.label_13.setText(_translate("FacialRigWindow", "Render", None))
        self.clearRender_pushButton.setText(_translate("FacialRigWindow", "Clear Render Nodes", None))
        self.anim_pushButton.setText(_translate("FacialRigWindow", "Rig Anim Face", None))
        self.save_pushButton.setText(_translate("FacialRigWindow", "Save File", None))
        self.clearAll_pushButton.setText(_translate("FacialRigWindow", "Clear All Nodes", None))
        self.label_14.setText(_translate("FacialRigWindow", "Anim", None))
        self.copyTexture_pushButton.setText(_translate("FacialRigWindow", "Copy Texture", None))
