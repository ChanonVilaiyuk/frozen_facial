#Import python modules
import maya.cmds as mc 
import sys, os, re
import subprocess

from datetime import datetime
sys.path.append('O:/studioTools/maya/python')

# Import GUI
from qtshim import QtCore, QtGui
from qtshim import Signal
from qtshim import wrapinstance

from tool.rig.facialTexture import ui
from tool.rig.facialTexture import facialTexture_app as facialCore
from tool.utils import fileUtils 
from tool.utils import pipelineTools as pt
reload(ui)
reload(facialCore)
reload(fileUtils)
reload(pt)

# from module import customLog
# logger = customLog.customLog()
# logger.setLevel(customLog.DEBUG)

moduleDir = sys.modules[__name__].__file__

# If inside Maya open Maya GUI

def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()

    if ptr is None:
        raise RuntimeError('No Maya window found.')

    window = wrapinstance(ptr)
    assert isinstance(window, QtGui.QMainWindow)
    return window

import maya.OpenMayaUI as mui
getMayaWindow()


class MyForm(QtGui.QMainWindow):

	def __init__(self, parent=None):
		self.count = 0
		#Setup Window
		super(MyForm, self).__init__(parent)
		self.ui = ui.Ui_FacialRigWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('PT Facial Texture Rig v.1.0')

		self.projectSkipKey = ['_', '.']
		self.projectPrefix = ['Lego']
		self.drive = 'P:/'
		self.info = pt.info()

		self.headBase = 'P:/Lego_Frozen/asset/3D/_base/head'
		self.defaultHeadName = 'head_ply'
		self.renderHeadName = 'headRenderStill_ply'
		self.previewHeadName = 'headAnimStill_ply'
		self.renderNode = 'headRender_vraymtl'
		self.animNode = 'headAnim_lmbt'
		self.stillGroup = 'headFacialStill_grp'
		self.texturePath = str()
		self.textureTemplate = 'P:/Lego_Frozen/asset/3D/_base/textures'

		self.initFunctions()
		self.initSignals()


	def initFunctions(self) : 
		self.setButtonStatus()
		self.browseBase()
		self.refreshUI()

	def setButtonStatus(self) : 
		self.ui.render_pushButton.setEnabled(False)
		self.ui.anim_pushButton.setEnabled(False)
		self.ui.save_pushButton.setEnabled(False)
		self.ui.open_pushButton.setEnabled(False)


	def refreshUI(self) : 
		# refresh UI 
		self.setProjectUI()
		self.setTypeUI()
		self.setSubTypeUI()
		self.listAssetUI()
		self.setPathUI()
		self.listWorkAreaUI()


	def initSignals(self) : 
		self.ui.project_comboBox.currentIndexChanged.connect(self.setTypeUI)
		self.ui.type_comboBox.currentIndexChanged.connect(self.setSubTypeUI)
		self.ui.subType_comboBox.currentIndexChanged.connect(self.listAssetUI)
		self.ui.asset_comboBox.currentIndexChanged.connect(self.setPathUI)

		# lineEdit 
		self.ui.path_lineEdit.textChanged.connect(self.listWorkAreaUI)

		# button 
		self.ui.import_pushButton.clicked.connect(self.doImportBase)
		self.ui.save_pushButton.clicked.connect(self.doSave)
		self.ui.open_pushButton.clicked.connect(self.doOpen)
		self.ui.render_pushButton.clicked.connect(self.doRenderRig)
		self.ui.anim_pushButton.clicked.connect(self.doAnimRig)
		self.ui.rig_pushButton.clicked.connect(self.doRigController)
		self.ui.clearRender_pushButton.clicked.connect(self.doClearRenderNode)
		self.ui.clearAnim_pushButton.clicked.connect(self.doClearAnimNode)
		self.ui.clearAll_pushButton.clicked.connect(self.doClearAllNode)
		self.ui.copyTexture_pushButton.clicked.connect(self.doCopyTexture)


	def setProjectUI(self) : 
		crProject = str()
		if self.info : 
			crProject = self.info['projectName']

		projects = fileUtils.listFolder(self.drive)
		self.ui.project_comboBox.clear()

		index = 0 
		i = 0 

		for each in projects : 
			if not each[0] in self.projectSkipKey and each.split('_')[0] in self.projectPrefix : 
				self.ui.project_comboBox.addItem(each)

				if each == crProject : 
					index = i 

				i += 1 

		self.ui.project_comboBox.setCurrentIndex(index)


	def setTypeUI(self) : 
		crType = str()
		if self.info : 
			crType = self.info['assetType']

		project = str(self.ui.project_comboBox.currentText())

		path = '%s%s/asset/3D' % (self.drive, project)
		types = fileUtils.listFolder(path)
		self.ui.type_comboBox.clear() 

		index = 0 
		i = 0 

		for each in types : 
			self.ui.type_comboBox.addItem(each)

			if crType == each : 
				index = i 

			i += 1 

		self.ui.type_comboBox.setCurrentIndex(index)


	def setSubTypeUI(self) : 
		crSubType = str() 
		if self.info : 
			crSubType = self.info['assetSubtype']

		project = str(self.ui.project_comboBox.currentText())
		selType = str(self.ui.type_comboBox.currentText())

		path = '%s%s/asset/3D/%s' % (self.drive, project, selType)
		subTypes = fileUtils.listFolder(path)

		self.ui.subType_comboBox.clear()

		i = 0 
		index = 0 

		for each in subTypes : 
			self.ui.subType_comboBox.addItem(each)

			if each == crSubType : 
				index = i 

			i += 1 

		self.ui.subType_comboBox.setCurrentIndex(index)


	def listAssetUI(self) : 
		crAsset = str() 
		if self.info : 
			crAsset = self.info['assetName']

		project = str(self.ui.project_comboBox.currentText())
		selType = str(self.ui.type_comboBox.currentText())
		selSubType = str(self.ui.subType_comboBox.currentText())

		path = '%s%s/asset/3D/%s/%s' % (self.drive, project, selType, selSubType)
		assets = fileUtils.listFolder(path)

		self.ui.asset_comboBox.clear()

		index = 0 
		i = 0 

		for each in assets : 
			self.ui.asset_comboBox.addItem(each)

			if each == crAsset : 
				index = i 

			i += 1 

		self.ui.asset_comboBox.setCurrentIndex(index)
		# self.ui.asset_comboBox.setCurrentRow(index)


	def setPathUI(self) : 
		project = str(self.ui.project_comboBox.currentText())
		selType = str(self.ui.type_comboBox.currentText())
		selSubType = str(self.ui.subType_comboBox.currentText())
		selAsset = str(self.ui.asset_comboBox.currentText())

		path = '%s%s/asset/3D/%s/%s/%s' % (self.drive, project, selType, selSubType, selAsset)
		self.ui.path_lineEdit.setText(path)


	def listWorkAreaUI(self) : 
		path = str(self.ui.path_lineEdit.text())
		rigPath = '%s/rig/maya/work' % (path)
		workFiles = fileUtils.listFile(rigPath)
		self.texturePath = '%s/textures' % (path)


		self.ui.work_listWidget.clear()

		for each in workFiles : 
			self.ui.work_listWidget.addItem(each)
		
		self.setRes(self.texturePath)

		if os.path.exists(rigPath) : 
			self.ui.open_pushButton.setEnabled(True)
			self.ui.save_pushButton.setEnabled(True)

	def browseBase(self) : 
		bases = fileUtils.listFile(self.headBase)

		self.ui.base_comboBox.clear()

		for each in bases : 
			self.ui.base_comboBox.addItem(each)


	def setRes(self, path) : 
		res = fileUtils.listFolder(path)

		self.ui.renderRes_comboBox.clear()
		self.ui.animRes_comboBox.clear()

		if res : 
			self.ui.render_pushButton.setEnabled(True)
			self.ui.anim_pushButton.setEnabled(True)

		i = 0 
		for each in res : 
			self.ui.renderRes_comboBox.addItem(each)
			self.ui.animRes_comboBox.addItem(each)

			i += 1 

		self.ui.renderRes_comboBox.setCurrentIndex(i-1)


	def doImportBase(self) : 
		selBase = str(self.ui.base_comboBox.currentText())
		path = '%s/%s' % (self.headBase, selBase)

		if not mc.objExists(self.defaultHeadName) : 
			mc.file(path, i = True)

		else : 
			self.messageBox('Base Exists', '"%s" already in the scene' % self.defaultHeadName)


	def doCopyTexture(self) : 
		src = self.textureTemplate 
		dst = self.texturePath

		res = fileUtils.listFolder(src)

		if os.path.exists(dst) : 
			try : 
				for each in res : 
					src2 = '%s/%s' % (src, each)
					dst2 = '%s/%s' % (dst, each)

					result = fileUtils.copyTree(src2, dst2)
					print result 

				self.messageBox('Complete', 'Copy Texture Complete')

			except Exception as e : 
				print e 
				self.messageBox('Error', str(e))


	def doSave(self) : 
		path = str(self.ui.path_lineEdit.text())
		rigPath = '%s/rig/maya/work' % (path)
		assetName = str(self.ui.asset_comboBox.currentText())
		nameKey = '%s_rig_facial' % assetName

		version = self.findVersion(rigPath, nameKey)
		user = mc.optionVar(q = 'PTuser')
		fileName = '%s_%s_%s.ma' % (nameKey, version, user)
		filePath = '%s/%s' % (rigPath, fileName)

		if not os.path.exists(filePath) : 
			mc.file(rename = filePath)
			mc.file(save = True)

		self.listWorkAreaUI()


	def doOpen(self) : 
		path = str(self.ui.path_lineEdit.text())
		rigPath = '%s/rig/maya/work' % (path)
		selFile = str(self.ui.work_listWidget.currentItem().text())

		openPath = '%s/%s' % (rigPath, selFile)

		if os.path.exists(openPath) : 
			mc.file(openPath, o = True, f = True, ignoreVersion = True)


	def doRenderRig(self) : 
		path = str(self.ui.path_lineEdit.text())
		texturePath = '%s/textures' % path 
		renderRes = str(self.ui.renderRes_comboBox.currentText())

		facialCore.path = texturePath
		facialCore.res = renderRes

		if mc.objExists(self.defaultHeadName) : 
			# rename 
			mc.rename(self.defaultHeadName, self.renderHeadName)

			# group 
			group = mc.group(em = True, n = self.stillGroup)
			mc.parent(self.renderHeadName, group)

			# render node 
			ltNode = facialCore.makeRenderFacial()

			# create lambert 
			if not mc.objExists(self.renderNode) : 
				vrayMtl = mc.shadingNode('VRayMtl', asShader = True, n = self.renderNode)

			# connect 
			mc.connectAttr('%s.outColor' % ltNode, '%s.color' % vrayMtl, f = True)

			# assign 
			mc.select(self.renderHeadName)
			mc.hyperShade(assign = vrayMtl)

			self.messageBox('Success', 'Set Render Node Complete')

		else : 
			self.messageBox('Warning', '%s not Exists' % self.defaultHeadName)


	def doAnimRig(self) : 
		path = str(self.ui.path_lineEdit.text())
		texturePath = '%s/textures' % path 
		animRes = str(self.ui.animRes_comboBox.currentText())

		facialCore.path = texturePath
		facialCore.animRes = animRes

		if mc.objExists(self.renderHeadName) : 
			previewHead = mc.duplicate(self.renderHeadName, n = self.previewHeadName)[0]

			# render node 
			ltNode = facialCore.makeAnimFacial(facialCore.renderLayerTextureName)

			# create lambert 
			if not mc.objExists(self.animNode) : 
				mtl = mc.shadingNode('lambert', asShader = True, n = self.animNode)

			# connect 
			mc.connectAttr('%s.outColor' % ltNode, '%s.color' % mtl, f = True)

			# assign 
			mc.select(previewHead)
			mc.hyperShade(assign = mtl)

			self.messageBox('Success', 'Set Anim Node Complete')


	def doRigController(self) : 
		facialCore.rigFacialCtrl()
		self.messageBox('Success', 'Rig controller complete')

	def doClearRenderNode(self) : 
		facialCore.clear('render')
		self.messageBox('Success', 'Clear render nodes complete')

	def doClearAnimNode(self) : 
		facialCore.clear('anim')
		self.messageBox('Success', 'Clear anim nodes complete')

	def doClearAllNode(self) : 
		facialCore.clear('all')
		self.messageBox('Success', 'Clear all nodes complete')


	def messageBox(self, title, description) : 
		# result = QtGui.QMessageBox.question(self,title,description ,QtGui.QMessageBox.AcceptRole, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
		result = QtGui.QMessageBox.question(self,title,description ,QtGui.QMessageBox.Ok)

		return result


	def findVersion(self, path, nameKey) : 
		files = fileUtils.listFile(path)
		versions = []

		for each in files : 
			if nameKey in each : 
				eles = each.split('_')

				for eachEle in eles : 
					if eachEle[0] == 'v' and eachEle[1:].isdigit() : 
						version = eachEle[1:]

						versions.append(int(version))

		if versions : 
			newVersion = 'v%03d' % (versions[-1] + 1)

		else : 
			newVersion = 'v001'

		return newVersion


# import sys 
# sys.path.append('O:/studioTools/maya/python')

# from tool.rig.facialTexture import facialTexture_app as app
# reload(app)

# app.path = 'P:/Lego_Frozen/asset/3D/character/main/frz_anna/textures'
# app.res = '4K'

# app.clear('all')
# app.makeRenderFacial()
# app.makeAnimFacial(app.renderLayerTextureName)
# app.rigFacialCtrl()