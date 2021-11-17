from detect_text import detect_text
from locate_bubbles import get_bubbles
from translate import translate_text

file_name = '003'

polys = get_bubbles(file_name=file_name)
texts = detect_text(file_name=file_name, polyLen=len(polys))
translated = translate_text(texts=texts)
print('translated', translated)
print('Done!')

