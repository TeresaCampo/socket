#!/usr/bin/env python3
import socket
import sys
import time

HOST='127.0.0.1'
PORT=int(sys.argv[1])

#creo la welcoming socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as welcomingSocket:
    #faccio bind
    welcomingSocket.bind((HOST,PORT))
    #faccio listen
    welcomingSocket.listen()
    #accetto richiesta connessione di un client
    conn, addr= welcomingSocket.accept()
    print("Connection established...client=",addr)
    #fai cose
    print("Connection closed...")
    time.sleep(1)