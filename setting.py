facialGrp = 'facialRig_grp'
facialCtrls = ['eyeLFT_ctrl', 'ebLFT_ctrl', 'eyeRGT_ctrl', 'ebRGT_ctrl', 'mouth_ctrl', 'highlightLFT_ctrl', 'highlightRGT_ctrl', 'eyeLidLFT_ctrl', 'eyeLidRGT_ctrl'] 
elements = ['base', 'L_baseEye', 'R_baseEye', 'L_eye', 'R_eye', 'L_eyeHighlight', 'R_eyeHighlight', 'L_eyeLash', 'R_eyeLash', 'L_brow', 'R_brow', 'mouth']

facialCtrlMap = {	'eyeLFT_ctrl': [{'node': 'L_eye', 'attr': [0, 1, 2]}], 
					'eyeRGT_ctrl': [{'node': 'R_eye', 'attr': [0, 1, 2]}], 
					'ebLFT_ctrl': [{'node': 'L_brow', 'attr': [0, 1, 2, 3]}], 
					'ebRGT_ctrl': [{'node': 'R_brow', 'attr': [0, 1, 2, 3]}], 
					'eyeLidLFT_ctrl': [{'node': 'L_eyeLid', 'attr': [0, 1, 2]}, {'node': 'L_baseEye', 'attr': [0, 1]}], 
					'eyeLidRGT_ctrl': [{'node': 'R_eyeLid','attr': [0, 1, 2]}, {'node': 'R_baseEye', 'attr': [0, 1]}], 
					'highlightLFT_ctrl': [{'node': 'L_eyeHighlight', 'attr': [0, 1, 2]}], 
					'highlightRGT_ctrl': [{'node': 'R_eyeHighlight', 'attr': [0, 1, 2]}], 
					'mouth_ctrl': [{'node': 'mouth', 'attr': [0, 1, 2, 3]}]
					}
