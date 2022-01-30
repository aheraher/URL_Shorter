import pyshorteners
from colorama import Fore
import sys

print(Fore.BLUE+"\tWelcome To URL Shorter By Dipu\n")

url = input(Fore.YELLOW+'Please Enter a URL :')
if not url:
    print(Fore.RED+"Faile ")
    sys.exit()
print(Fore.GREEN+"\n\tChoose a 1 option from follwing .")
print("1.URL SHORT\n2.URL EXPAND")
s = pyshorteners.Shortener()
choose = int(input())
if choose == 1:
    print(Fore.LIGHTYELLOW_EX+'you choose option 1')
    print("Your url is start to creat ")
    s = s.tinyurl.short(url)

    print("URL IS ", s)
elif choose == 2:
    print(Fore.LIGHTYELLOW_EX+"you choose option 2")
    print("Your url is start to creat ")

    s = s.tinyurl.expand(url)
    print("URL IS ", s)
print(Fore.CYAN+"Thank for use us \U0001F600 ")
