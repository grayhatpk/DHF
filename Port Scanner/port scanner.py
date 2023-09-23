#!/usr/bin/python3

import socket
import sys

#creating a connection

IP = sys.argv[1] # first argument is Ip address to scan 
sport = int(sys.argv[2]) # starting port  number 
eport = int(sys.argv[3]) # ending port number 

for i in range(sport,eport+1):  #port range 

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	socket.setdefaulttimeout(2)
	
	response = s.connect_ex((IP,i))
	
	if response == 0:
		print("\n The port {} is closed ".format(i))
	else:
		print("\n The port {} is OPEN ".format(i))
		s.close()
