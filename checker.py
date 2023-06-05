import requests
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
                x = requests.get(url+line, timeout=5)
                print(f'{url+line} = {x.status_code}')
    else:
        start()

start()
