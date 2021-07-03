import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

for i in range(15):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()

print(Fore.LIGHTYELLOW_EX)
menuprincipal = int(input("Main menu:  \n [1] Search info \n [2] Info the ip \n [!] Select option: "))
while menuprincipal != 0:
    if menuprincipal == 1:
        print(Fore.LIGHTCYAN_EX)
        searchinfo = input("Name for search: ")
        print(Fore.LIGHTRED_EX)
        print("https://facebook.com/" + (searchinfo))
        print("https://instagram/" + (searchinfo))
        print("https://youtube/" + (searchinfo))
        print("https://twitter/" + (searchinfo))
        print("https://twitch.tv/" + (searchinfo))
        print("https://facebook.com/" + (searchinfo))
        print("https://facebook.com/" + (searchinfo))
        print("https://facebook.com/" + (searchinfo))
        print(Fore.LIGHTYELLOW_EX)
    menu2 = int(input("Main menu:  \n [1] Search info \n [2] Info the ip \n [!] Select option: "))
    while menu2 != 0:
        if menu2 == 2:
             print(Fore.LIGHTCYAN_EX)
        infoip = input("ip for info: ")
        print(Fore.LIGHTRED_EX)
        print(f"the ip is the: https://es.geoipview.com/?q={infoip}&x=15&y=10")
        print(f"Info: https://es.infobyip.com/ip-{infoip}.html")
        print(Fore.RESET)
        print("FINISH :) ")