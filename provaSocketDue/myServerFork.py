#!/usr/bin/env python3
import socket
import sys
import time
import os
import re

HOST='127.0.0.1'
PORT=1025
def sendError(conn, addr):
	conn.sendall("ERROR".encode('utf-8'))
	print("Connection closed...")
	sys.exit()

def resolve(addressInFormat,netMask, negNetMask):
	netID=[addressInFormat[0]&netMask[0],
		addressInFormat[1]&netMask[1],
		addressInFormat[2]&netMask[2],
		addressInFormat[3]&netMask[3]]
	print(netID)

	broadcast=[addressInFormat[0]|negNetMask[0],
	addressInFormat[1]|negNetMask[1],
	addressInFormat[2]|negNetMask[2],
	addressInFormat[3]|negNetMask[3]]
	print(broadcast)
	
	broadcastString=''
	for i in broadcast:
		broadcastString=broadcastString+ str(i)+'.'
		

	netIDString=''
	for i in netID:
		netIDString= netIDString+str(i)+'.'
	return netIDString,broadcastString


def handleClient(conn, addr):
	data = conn.recv(256).decode('utf-8')
	data = data.split('\n',1)[0]
	data=data.split('.')
	if len(data)!=4:
		sendError(conn,addr)
	addressInFormat=[int(data[0]), int(data[1]), int(data[2]), int(data[3])]
	print(addressInFormat)
	for byte in addressInFormat:
		if (byte > 255) or (byte <0):
			sendError(conn,addr)
	firstByte=addressInFormat[0]
	
	if firstByte>>7 == 0:
		netMask=[255,0,0,0]
		negNetMask=[0,255,255,255]
		netID,broadcast=resolve(addressInFormat,netMask,negNetMask)
		conn.sendall(f'A {netID} {broadcast}'.encode('utf-8'))
	if firstByte>>6 == 2:
		netMask=[255,255,0,0]
		negNetMask=[0,0,255,255]
		netID,broadcast=resolve(addressInFormat,netMask,negNetMask)
		conn.sendall(f'B {netID} {broadcast}'.encode('utf-8'))
	if firstByte>>5 == 6:
		netMask=[255,255,255,0]
		negNetMask=[0,0,0,255]
		netID,broadcast=resolve(addressInFormat,netMask,negNetMask)
		conn.sendall(f'C {netID} {broadcast}'.encode('utf-8'))
	if firstByte>>4 == 14:
		conn.sendall("D".encode('utf-8'))
	if firstByte>>4 == 15:
		conn.sendall("E".encode('utf-8'))

def main():
	#creo la welcoming socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as welcomingSocket:
	    #faccio bind
		welcomingSocket.bind((HOST,PORT))
	    #faccio listen
		welcomingSocket.listen()
		while True:
			#accetto richiesta connessione di un client
			conn,addr= welcomingSocket.accept()
			pid=os.fork()
			if pid==0:
				print("Connection established...client=",addr)
				handleClient(conn,addr)
				print("Connection closed...")
				sys.exit()
			else: 
				conn.close()
				os.wait()
				time.sleep(1)
            
if __name__ == "__main__":
    main()