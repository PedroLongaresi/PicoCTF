from base64 import b64decode
from base64 import b64encode

import requests


def bitFlip(pos, bit, data):
    # pos = pos + 1
    raw = b64decode(data)
    print(pos)
    list1 = list(raw)
    print(ord(list1[pos]) ^ bit)
    list1[pos] = chr(ord(list1[pos]) ^ bit)
    raw = ''.join(list1)
    return b64encode(raw)


    ck = "RkdsVTVoWksxbmFPbFNKT2liNUJYWjFTWTMzNDBsb2Z0U245SWx5TTJtVUpRNDgyRTlHanBzQjUyUUp3dVJqWk1DdTlOSE12Zm5veHJTalMrcXpkbHpxdTNzakNqTUxvVkRyNGhHWHBMN2x2eUdVYm80LzRIOWkzMHZEOFJPNnk="

    for i in range(128):
        for j in range(128):
            print(i)
            c = bitFlip(i, j, ck)
            cookies = {'auth_name': c}
            r = requests.get('http://mercury.picoctf.net:21553/', cookies=cookies)
            if "picoCTF{" in r.text:
                print(r.text)
                break
