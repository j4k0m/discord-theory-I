# Usage: python3 sorting.py [CODE]
import re, base64, sys

def sorting(code):
    list = [ord(chr(eval(j))) for j in ['0x'+ i for i in re.findall('..', base64.b64decode(code).hex())]]
    ex = []
    no = []
    for i in list:
        if i >= 0 and i <= 127:
            no.append(i)
        elif i >= 128 and i <= 255:
            ex.append(i)
    print(f"Extended: {' '.join(map(hex, ex))}")
    print(f"Normal: {' '.join(map(hex, no))}")
    print(f"Extended: {len(ex)}, Normal: {len(no)}")
    
sorting(sys.argv[1])
