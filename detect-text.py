from PIL import Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def get_params():
    params = ""
    params += "--psm 12"

    configParams = []
    def configParam(param, val):
      return "-c " + param + "=" + val

    configParams.append(("chop_enable", "T"))
    configParams.append(('use_new_state_cost','F'))
    configParams.append(('segment_segcost_rating','F'))
    configParams.append(('enable_new_segsearch','0'))
    configParams.append(('textord_force_make_prop_words','F'))
    configParams.append(('tessedit_char_blacklist', '}><L'))
    configParams.append(('textord_debug_tabfind','0'))
    params += " ".join([configParam(p[0], p[1]) for p in configParams])
    return params

print('0', pytesseract.image_to_string('cv2-output-001/bubble-0.png', lang='jpn_vert', config=get_params()))
print('1', pytesseract.image_to_string('cv2-output-001/bubble-1.png', lang='jpn_vert', config=get_params()))
print('2', pytesseract.image_to_string('cv2-output-001/bubble-2.png', lang='jpn_vert', config=get_params()))
print('3', pytesseract.image_to_string('cv2-output-001/bubble-3.png', lang='jpn_vert', config=get_params()))
print('4', pytesseract.image_to_string('cv2-output-001/bubble-4.png', lang='jpn_vert', config=get_params()))
print('5', pytesseract.image_to_string('cv2-output-001/bubble-5.png', lang='jpn_vert', config=get_params()))