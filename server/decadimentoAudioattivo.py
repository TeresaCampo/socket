#!/usr/bin/env python3
import socket
import sys
import time
import os
import re 

HOST='127.0.0.1'
PORT=8080
def inputCheck(data):
	data=data.split('\r\n',1)[0]
	seed=data.split(',',1)[0]
	niterations=data.split(',',1)[1]

	patternSeed=r'^\d$'
	if not re.match(patternSeed,seed):
		return False		
	patternNiterations=r'^\d+$'
	if not re.match(patternNiterations, niterations):
		return False
	return True

def algorithm(seed,niterations,conn):
	output=seed
	for iterations in range(niterations):
		newOutput=""
		indexInString=0
		startCurrentNumber=0
		currentNumber=output[indexInString]
		for indexInString in range(len(output)+1):
			print(f'current index {indexInString} and current number {currentNumber}')
			if indexInString==len(output):
				repetitionsCurrentNumber=output[startCurrentNumber:indexInString].count(currentNumber)
				newOutput=newOutput+str(repetitionsCurrentNumber)+str(currentNumber)
				continue
			if currentNumber==output[indexInString]:
				continue
			else:
				repetitionsCurrentNumber=output[startCurrentNumber:indexInString].count(currentNumber)
				newOutput=newOutput+str(repetitionsCurrentNumber)+str(currentNumber)
				currentNumber=output[indexInString]
				startCurrentNumber=indexInString
		
		conn.sendall(f'{newOutput}\r\n'.encode('utf-8'))
		output=newOutput
		newOutput=""

def handleClient(conn):
	data= conn.recv(256).decode('utf-8')
	if not inputCheck(data):
		print("Wrong input format")
		conn.sendall(f"-ERR\r\n".encode('utf-8'))
		return
	seed=data.split(',',1)[0]
	niterations=int(data.split(',',1)[1])
	conn.sendall(f"+OK {niterations} iterations on seed {seed}\r\n".encode('utf-8'))
	algorithm(seed,niterations, conn)



def main():
	#creo la welcoming socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as welcomingSocket:
		#faccio bind
		welcomingSocket.bind((HOST,PORT))
		#faccio listen
		welcomingSocket.listen()
		while True:
			#accetto richiesta connessione di un client
			conn, addr= welcomingSocket.accept()
			pid=os.fork()
			if pid==0:
				print("Connection established...client=",addr)
				handleClient(conn)
				print("Connection closed...")
				sys.exit()
			else: 
				conn.close()
				os.wait()
		time.sleep(1)

if __name__ == "__main__":
    main()