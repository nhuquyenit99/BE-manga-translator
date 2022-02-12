import subprocess
from multiprocessing.pool import ThreadPool as Pool
import re
import json

def translate_single(text: str, index: int, result: list):
    bs = subprocess.check_output(["node", "translate.js", text])
    # print('translated', bs)
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

# result = translate_text(['こんにちは', '店長 ! こ れ ボク の エプロ ン'])
# print('result', result)
