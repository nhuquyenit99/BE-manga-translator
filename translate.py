import subprocess
from multiprocessing.pool import ThreadPool as Pool
import re

def translate_single(text: str, index: int, result: list):
    txt = re.sub(r"\n", "", text)
    bs = subprocess.check_output(["node", "translate.js", txt])
    print('translated', bs)
    result[index] = bs
    return bs


def translate_text(texts: list):
    pool = Pool(len(texts))
    result = ['']*len(texts)
    for index, text in enumerate(texts): 
        pool.apply_async(translate_single, (text, index, result))
    pool.close()
    pool.join()
    return result



# def translate_text(texts: list):
#     result = []
#     for text in texts: 
#         txt = re.sub(r"\n", "", text)
#         print('text', text)
#         bs = subprocess.check_output(["node", "translate.js", text])
#         result.append(bs)
#     return result

result = translate_text(['こんにちは', 'はじめまして', 'あなたはとても美しいです', 'あなたはとても美しいです', 'あなたはとても美しいです', 'あなたはとても美しいです', 'あなたはとても美しいです', 'あなたはとても美しいです','あなたはとても美しいです','あなたはとても美しいです'])
print('result', result)
