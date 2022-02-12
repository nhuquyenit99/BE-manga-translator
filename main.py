from detect_text import detect_text
from locate_bubbles import get_bubbles
from translate import translate_text
from craft import craft_text
import uuid

def translate_manga(image_path: str, file_name: str, page: int):
    craft_text(image_url=image_path, file_name=file_name)
    polys = get_bubbles(file_name=file_name)
    texts = detect_text(file_name=file_name, polyLen=len(polys))
    translated = translate_text(texts=texts)
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


