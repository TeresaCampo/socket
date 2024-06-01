#!/usr/bin/env python3
import socket
import sys
import time
import os

HOST='127.0.0.1'
PORT=2525

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
            message= "Welcome from "+socket.gethostname()
            conn.sendall(message.encode('utf-8'))
            print("Connection closed...")
            sys.exit()
        else: conn.close()
    time.sleep(1)