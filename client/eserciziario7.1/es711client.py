#!/usr/bin/env python3
import socket
import sys


if len(sys.argv)!= 2:
    print("ERROR: the function accept 1 parameter(hostname)")
    sys.exit(1)

HOST=sys.argv[1]
PORT=2525
FORMAT = "utf-8"

#creo socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    #creo connessione
    socket.connect((HOST,PORT))
    print("Connession established...")
    #fai cose
    data=socket.recv(256)
    print(data.decode(FORMAT))
    print("Closing connection...")
    #chiudo la connessione
    socket.close()
