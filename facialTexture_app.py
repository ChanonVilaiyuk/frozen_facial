import os, sys 
import maya.cmds as mc

from tool.utils import mNode as mNode
reload(mNode)

from tool.utils import fileUtils
reload(fileUtils)

from tool.rig.facialTexture import setting
reload(setting)

# change setting here 
path = 'P:/Lego_Frozen/asset/3D/character/main/frz_rnd/textures'
res = '4K'
animRes = '1K'
# facialCtrl = 'O:/studioTools/template/Lego_Frozen/rig/facial_ctrl.ma'
facialCtrl = 'P:/Lego_Frozen/asset/3D/_base/ctrl/facial_ctrl.ma'

# naming setting 
renderLayerTextureName = 'facialRender_lt'
animLayerTextureName = 'facialAnim_lt'
masterLoc = 'facialCtrl_loc'
startImg = 1

# layers 
elements = ['base', 'L_baseEye', 'R_baseEye', 'L_eye', 'R_eye', 'L_eyeHighlight', 'R_eyeHighlight', 'L_eyeLid', 'R_eyeLid', 'L_brow', 'R_brow', 'mouth', 'extra']

elementMaps = {'base': {'mode': 0, 'attr': ['X', 'Y', 'switch']}, 
						'L_baseEye': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'R_baseEye': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'L_eye': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'R_eye': {'mode': 1, 'attr': ['X', 'Y', 'switch']},
						'L_eyeHighlight': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'R_eyeHighlight': {'mode': 1, 'attr': ['X', 'Y', 'switch']},  
						'L_eyeLid': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'R_eyeLid': {'mode': 1, 'attr': ['X', 'Y', 'switch']}, 
						'L_brow': {'mode': 1, 'attr': ['X', 'Y', 'switch', 'swing']}, 
						'R_brow': {'mode': 1, 'attr': ['X', 'Y', 'switch', 'swing']}, 
						'mouth': {'mode': 1, 'attr': ['X', 'Y', 'switch', 'swing']},
						'extra': {'mode': 1, 'attr': ['X', 'Y', 'switch', 'swing']}
						}


locAttr = ['X', 'Y', 'switch', 'swing']
ctrlMap = {'X': {'node': 'place2dTexture', 'attr': 'translateFrameU', 'dv': 0, 'limit': False, 'amp': 0.5}, 
			'Y': {'node': 'place2dTexture', 'attr': 'translateFrameV', 'dv': 0, 'limit': False, 'amp': 0.5}, 
			'switch': {'node': 'file', 'attr': 'frameExtension', 'dv': 1, 'limit': True, 'amp': 1}, 
			'swing': {'node': 'place2dTexture', 'attr': 'rotateUV', 'dv': 0, 'limit': False, 'amp': -1}
			}


def makeRenderFacial(makeElements = elements, force = True) : 
	info, missing = checkElements()
	name = renderLayerTextureName

	# if layeredTexture exists 
	if mc.objExists(name) : 
		# instance 
		ltNode = mNode.layeredTexture(name)

		# clear matte channel
		ltNode.cleanAllMatte()

	# if not exists 
	else : 
		# instance new layeredTexture
		ltNode = mNode.layeredTexture()
		ltNode.setName(name)

	# add texture to list
	for each in reversed(makeElements) : 

		# if elements exists, continue 
		if each in info.keys() : 
			filepath = info[each]['path']
			mode = elementMaps[each]['mode']
			nodeAttr = elementMaps[each]['attr']

			addLayerTexture(filepath, ltNode, mode, nodeAttr, True, True)


	return ltNode


def makeAnimFacial(renderTextureNode) : 
	# instance renderNode
	renderNode = mNode.layeredTexture(renderTextureNode)
	nodes = renderNode.listTextures()
	indexs = renderNode.listIndexs()

	# create anim render layer
	if mc.objExists(animLayerTextureName) : 
		mc.delete(animLayerTextureName) 

	ltNode = mNode.layeredTexture()
	ltNode.setName(animLayerTextureName)

	# clear all aFile nodes 
	mc.delete(mc.ls('*aFile'))

	# loop each connected node 
	index = 0 
	ii = 0 

	for node in nodes : 
		# instance file node 
		fileNode = mNode.fileNode(node)
		filePath = fileNode.getFileName()
		files = getFileSequences(filePath)

		# find connection to image sequences
		switchAttr = mc.listConnections('%s.frameExtension' % fileNode, p = True)

		# find index 
		blendMode = renderNode.getBlendMode(indexs[ii])

		# find placement and instance 
		plc = fileNode.findPlacement()

		if plc : 
			plcNode = mNode.placementNode(plc[0])

		else : 
			plcNode = mNode.placementNode()

		# loop each files in node
		i = 0 

		for eachFile in files : 
			num = findNum(eachFile)
			fileNodeName = '%s_%s_aFile' % (node, num)
			cndNodeName = '%s_%s_aCnd' % (node, num)
			filePath = eachFile.replace(res, animRes) 

			# create file node 
			fileNode = mNode.fileNode()
			fileNode.setName(fileNodeName)
			fileNode.setFileName(filePath)

			# turn off filter 
			fileNode.setFilter(0)

			# add to layeredTexture 
			ltNode.addTexture(fileNode, index)
			ltNode.setBlendMode(index, blendMode)

			# connected placement 
			plcNode.connectFileNode(fileNode)

			# connect switch attr 
			if switchAttr : 
				cndNode = mNode.condition()
				cndNode.setName(cndNodeName)
				cndNode.connectFirstTerm(switchAttr[0])
				cndNode.setSecondTerm(int(num))
				cndNode.setColorIfTrue(1, 1, 1)
				cndNode.setColorIfFalse(0, 0, 0)

				# link to visible state of layeredTexture 
				targetAttr = '%s.inputs[%s]isVisible' % (ltNode, index)
				cndNode.connectOutput('red', targetAttr)

				i += 1 

			index += 1 

		ii += 1 

	return ltNode

def checkElements() : 
	missing = []
	info = dict()

	for each in elements : 
		dir = '%s/%s/%s' % (path, res, each)

		if os.path.exists(dir) : 
			files = fileUtils.listFile(dir)
			heroFrame = ''

			for eachFile in files : 
				num = findNum(eachFile)

				if num : 
					if startImg == int(num) : 
						heroFrame = eachFile 

			if heroFrame : 
				info[each] = {'filename': heroFrame, 'path': '%s/%s' % (dir, heroFrame)}

			if not heroFrame : 
				missing.append(each)

	if missing : 
		for each in missing : 
			print 'missing file in dir %s' % each 

		print '=============='
		print '%s dir' % len(missing)


	return info, missing


def addLayerTexture(filepath, nodeName, mode, nodeAttr, addCtrl = False, force = False) : 
	# if path exists 
	if os.path.exists(filepath) : 
		ltNode = mNode.layeredTexture(nodeName)

		# subdir as node name 
		filepath = filepath.replace('\\', '/')
		name = filepath.split('/')[-2]
		nodeName = '%s_rFile' % name
		plcName = '%s_rPlc' % name

		state = True 

		if mc.objExists(nodeName) : 
			state = force

		if state : 

			# create file node 
			fileNode = mNode.fileNode()
			fileNode.setName(nodeName)
			fileNode.setFileName(filepath)

			# turn off filter 
			fileNode.setFilter(0)

			# find last index 
			indexs = ltNode.listIndexs()
			lastIndex = 1

			if indexs : 
				lastIndex = indexs[-1] + 1 

				# remove matte color if exists 
				if 0 in indexs : 
					if ltNode.isMatteColor(0) : 
						ltNode.removeTexture(0)

			ltNode.addTexture(fileNode, lastIndex)
			ltNode.setBlendMode(lastIndex, mode)

			# add placement 
			plcNode = mNode.placementNode()
			plcNode.setName(plcName)
			plcNode.connectFileNode(fileNode)

			if addCtrl : 
				addController(name, fileNode, plcNode, nodeAttr)


def addController(name, fileNode, plcNode, nodeAttr) : 
	print name 

	# create locator 
	if not mc.objExists(masterLoc) : 
		locator = mNode.locator()
		locator.setName(masterLoc)

	else : 
		locator = mNode.locator(masterLoc)

	locatorShape = mNode.dagNode('locator', locator.shape())

	i = 0
	nodeCount = 0
	channel = ['X', 'Y', 'Z']

	# loop create each attribute 
	for attr in nodeAttr : 
		attrName = '%s%s' % (name, attr)
		srcAttr = '%s.%s' % (locator, attrName)
		attrAmp = '%s_amp' % attrName

		node = ctrlMap[attr]['node']
		targetAttr = ctrlMap[attr]['attr']
		dv = ctrlMap[attr]['dv']
		mdvValue = ctrlMap[attr]['amp']
		limit = ctrlMap[attr]['limit']


		# create mdv amp 
		mdvChannel = channel[i%3]
		mdvName = '%s%s_rMdv' % (name, nodeCount)

		if i%3 == 0 : 			
			nodeCount += 1 
			mdvName = '%s%s_rMdv' % (name, nodeCount)
			ampNode = mNode.mulNode()
			ampNode.setName(mdvName)

		else : 
			if mc.objExists(mdvName) : 
				ampNode = mNode.mulNode(mdvName)


		# add attr
		if not mc.objExists(srcAttr) : 
			# switch facial limit 1 
			if limit : 
				srcAttr = locator.addAttr('double', attrName, min = dv, dv = dv) 

			# other attrs no limit 
			if not limit : 
				srcAttr = locator.addAttr('double', attrName, dv = dv) 

		# add amp 
		if not mc.objExists('%s.%s' % (locatorShape, attrAmp)) : 
			locatorShape.addAttr('double', attrAmp)


		targetNode = None

		# connect attribute 
		if node == 'file' : 
			fileNode.useSequence(1)
			fileNode.clearSequenceExpression()
			targetNode = fileNode 

		if node == 'place2dTexture' : 
			targetNode = plcNode

		if targetNode : 
			ampNode.connect(mdvChannel, srcAttr, '%s.%s' % (targetNode, targetAttr), mdvValue)
			locatorShape.connect(attrAmp, ampNode.attribute('input2', mdvChannel))
			locatorShape.setAttr(attrAmp, mdvValue)

			i += 1 

def rigFacialCtrl() : 
	# import facial 
	facialGrp = setting.facialGrp
	facialCtrlMap = setting.facialCtrlMap

	if not mc.objExists(facialGrp) : 
		mc.file(facialCtrl, i = True, pr = True)

	if mc.objExists(masterLoc) : 
		for eachCtrl in facialCtrlMap.keys() : 
			attrNames = facialCtrlMap[eachCtrl]
			
			for eachAttr in attrNames : 
				attrName = eachAttr['node']
				attrs = eachAttr['attr']

				if 0 in attrs : 
					dst = '%s.%s%s' % (masterLoc, attrName, locAttr[0])
					if mc.connectionInfo(dst, isDestination=True) : 
						mc.delete(dst, icn = True)

					mc.connectAttr('%s.translateX' % eachCtrl, dst, f = True)
					# print eachCtrl, '%s.%s%s' % (masterLoc, attrName, locAttr[0])

				if 1 in attrs : 
					dst = '%s.%s%s' % (masterLoc, attrName, locAttr[1])
					if mc.connectionInfo(dst, isDestination=True) : 
						mc.delete(dst, icn = True)

					mc.connectAttr('%s.translateY' % eachCtrl, dst, f = True)
					# print eachCtrl, '%s.%s%s' % (masterLoc, attrName, locAttr[1])

				if 2 in attrs : 
					dst = '%s.%s%s' % (masterLoc, attrName, locAttr[2])
					if mc.connectionInfo(dst, isDestination=True) : 
						mc.delete(dst, icn = True)

					mc.connectAttr('%s.shape' % eachCtrl, dst, f = True)
					# print eachCtrl, '%s.%s%s' % (masterLoc, attrName, locAttr[2])

				if 3 in attrs : 
					dst = '%s.%s%s' % (masterLoc, attrName, locAttr[3])
					if mc.connectionInfo(dst, isDestination=True) : 
						mc.delete(dst, icn = True)

					mc.connectAttr('%s.swing' % eachCtrl, dst, f = True)
					# print eachCtrl, '%s.%s%s' % (masterLoc, attrName, locAttr[3])


def clear(nodeType) : 
	if nodeType == 'anim' : 
		mc.delete(mc.ls('*_aFile'))
		mc.delete(mc.ls('*_aCnd'))

		if mc.objExists(animLayerTextureName) : 
			mc.delete(animLayerTextureName)

	if nodeType == 'render' : 
		mc.delete(mc.ls('*_rFile'))
		mc.delete(mc.ls('*_rPlc'))
		mc.delete(mc.ls('*_rMdv'))

		if mc.objExists(renderLayerTextureName) : 
			mc.delete(renderLayerTextureName)

	if nodeType == 'all' : 
		clear('anim')
		clear('render')




def findNum(name, padding = False) : 

	revName = name[::-1]
	strNum = ''
	read = False 
	numPos = []

	i = 0 
	for each in revName : 
	    if each == '.' : 
	        read = True 
	       
	    if read : 
	        if not each == '.' : 
	            if each.isdigit() : 
	                strNum += each
	                numPos.append(i)
	                
	            else : 
	                break

	    i += 1 

	if not padding : 
		returnValue = strNum[::-1]

	else : 
		returnValue = numPos

	return returnValue


def getFileSequences(fileName) : 
	dir = os.path.dirname(fileName) 
	files = fileUtils.listFile(dir)
	sequences = []
	pos = findNum(fileName, True)
	fileName[-pos[-1] - 1: -pos[0]]

	for each in files : 
		num = each[-pos[-1] - 1: -pos[0]]

		if num.isdigit() : 
			sequences.append('%s/%s' % (dir, each))

	return sequences
