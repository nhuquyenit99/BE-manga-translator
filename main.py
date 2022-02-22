from detect_text import detect_text
from locate_bubbles import get_bubbles
from translate import translate_text
from craft import craft_text
import uuid
import re

def translate_manga(image_path: str, file_name: str, page: int, lang: str = 'en'):
    craft_text(image_url=image_path, file_name=file_name)
    polys = get_bubbles(file_name=file_name)
    texts = detect_text(file_name=file_name, polyLen=len(polys))
    processed_texts = []
    for text in texts: 
        print('detect text', text)
        txt = re.sub(r"\n", "", text)
        txt = re.sub(" ", "", txt)
        print('processed text', txt)
        processed_texts.append(txt)

    translated = translate_text(texts=processed_texts, lang=lang)
    results = []
    for idx in range(len(polys)):
        id = uuid.uuid1()
        print(translated[idx]) 
        result = {
            "id": id,
            "poly": polys[idx].__dict__,
            "original_text": texts[idx],
            "translated_text": translated[idx],
            "page": page
        }
        results.append(result)
    return results


