from PIL import Image
from numpy import number
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

# use tesseract to detect text
def detect_text(file_name: str, polyLen: number):
  texts = []
  for idx in range(polyLen):
      text = pytesseract.image_to_string(Image.open('cv2-output/{}/bubble-{}.png'.format(file_name, idx)), lang='jpn_vert', config=get_params())
      texts.append(text)
      print('bubble', idx, ":", text)
  return texts

# detect_text("001", 6)

