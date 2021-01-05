import requests
import sys
import random
from colorama import Fore
from colorama import Style
import time
import re
from urllib.parse import urlparse









####### Colors     ######

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT


#######################
def logo():
    clear = "\x1b[0m"
    colors = [32]

    x = """
                          Do or Die 
                {"_/"}Viewdns Cleaner{"_/"}
	 ____  _       _____ _        ____ _____      _ _ 
	| __ )| | __ _|___ /| | __   |  _ \___ /_   _(_) |
	|  _ \| |/ _` | |_ \| |/ /   | | | ||_ \ \ / / | |
	| |_) | | (_| |___) |   <    | |_| |__) \ V /| | |
	|____/|_|\__,_|____/|_|\_\___|____/____/ \_/ |_|_|
	   Copyright:2021      |_____| Version: 1.0.0				                

        \033[0;37;41mCoded by Bla3k_D3vil 
        \033[0;37;41mICQ:https://icq.im/Bla3k_D3vil1
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

urls = str(input("Enter Your List :"))
with open(urls, 'r') as urls:
	for line in urls:
		url = line.rstrip() and line.split('\t')

		bond = url[0].replace('...', '')
		benz = url[0].split('/')
		clean = benz[0]
		if 'http://' not in clean:
			url = 'http://'+clean
			with open('cleaned.txt', 'a') as myfile:
			 myfile.write('http://'+clean)
			 myfile.write('\n')







