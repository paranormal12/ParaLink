import requests
import time
from colorama import init, Fore
init(convert=True)
def checker():
    print(Fore.RED + ' ██▓███   ▄▄▄       ██▀███  ▄▄▄      ███▄    █ ▒█████   ██▀███   ███▄ ▄███▓ ▄▄▄       ██▓    ')
    time.sleep(0.2)
    print(Fore.RED + '▓██░  ██▒▒████▄    ▓██ ▒ ██▒████▄    ██ ▀█   █▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒    ')
    time.sleep(0.2)
    print(Fore.RED + '▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒██  ▀█▄ ▓██  ▀█ ██▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄  ▒██░    ')
    time.sleep(0.2)
    print(Fore.RED + '▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄ ░██▄▄▄▄██▓██▒  ▐▌██▒██   ██░▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██ ▒██░    ')
    time.sleep(0.2)
    print(Fore.RED + '▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒▓█   ▓██▒██░   ▓██░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒░██████▒')
    time.sleep(0.2)
    print(Fore.RED + '▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▒   ▓▒█░ ▒░   ▒ ▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░')
    time.sleep(0.2)
    print(Fore.RED + '░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░ ▒   ▒▒ ░ ░░   ░ ▒░ ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░')
    time.sleep(0.2)
    print(Fore.RED + '░░         ░   ▒     ░░   ░  ░   ▒     ░   ░ ░░ ░ ░ ▒    ░░   ░ ░      ░     ░   ▒     ░ ░   ')
    time.sleep(0.2)
    print(Fore.RED + '               ░  ░   ░          ░  ░        ░    ░ ░     ░            ░         ░  ░    ░  ░')
    time.sleep(0.2)
    print('============================================================================================== ')
checker()

urls = input('Enter The File Urls : ')
with open(urls, 'r') as ink:
    
    for row in ink:
        row = row.strip()
        try:
            ve = requests.get(row).status_code
            if ve == 200: 
                print(Fore.GREEN + row, '==> Live')
                live = open('Live.txt', 'a')
                live.write(row + '\n')
        except:
                print(Fore.YELLOW + row, '==> Dead')
                live = open('Dead.txt', 'a')
                live.write(row + '\n')

print(Fore.MAGENTA + '\nAll Urls Are Saved.. Goodbye :)')