import subprocess
import re

def translate_text(texts: list):
    result = []
    for text in texts: 
        txt = re.sub(r"\n", "", text)
        print('text', text)
        bs = subprocess.check_output(["node", "translate.js", text])
        result.append(bs)
    return result
