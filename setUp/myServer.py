#!/usr/bin/env python3
import socket
import os
import sys
import argparse

HOST=sys.argv[1]
PORT=int(sys.argv[2])

def handleClient(conn, addr):
    #data= conn.recv(256)
    #print(data.decode('utf-8'))
    #message="Connection from "+socket.gethostname()
    #conn.sendall("ciao".encode('utf-8'))
    pass

def main():
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
        handleClient(conn,addr) #<------------------gestisci richiesta client qui dentro
        print("Connection closed...")
        time.sleep(1)

if __name__ == "__main__":
    main()
