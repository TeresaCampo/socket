#!/usr/bin/env python3
import socket
import sys
import time

HOST='127.0.0.1'
PORT=2525

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
    data= conn.recv(256)
    print(data.decode('utf-8'))
    #conn.sendall("ciao".encode('utf-8'))
    print("Connection closed...")
    time.sleep(1)