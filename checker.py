import requests
from requests.exceptions import ConnectTimeout
def start():
    print("choose an option: \n (0) = Add path \n (1) = check website")
    inp = input()
    if inp == "0":
        url = input("input path e.x. /index.html :")
        with open('urls.txt','a', encoding='UTF-8') as f:
            f.write(f"{url}\n")
    elif inp == "1":
        url = input("input target URL: ")
        with open('urls.txt','r', encoding='UTF-8') as f:
            for line in f:
                s = url + line
                s.replace(" ", "")
                try:
                    x = requests.get(s, timeout=5)
                    print(f'{s} ↳{x.status_code}')
                except ConnectTimeout:
                    print(f'{s} ↳Timeout')
    else:
        start()

start()
