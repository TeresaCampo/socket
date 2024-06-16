#!/usr/bin/env python3
import socket
import sys

PORT=1025

def handleClient(s, address):
        s.sendall(address.encode('utf-8'))
        data= s.recv(256).decode('utf-8')
        print(data.split('\n')[0])
        #print(data.decode('utf-8'))
        #message="Connection from "+ socket.gethostname()
        

def main():
    #check parametri
    if len(sys.argv)!= 3:
        print("ERROR: the function accept two ordered parameters(server,IPv4 address)")
        sys.exit(1)
    HOST=sys.argv[1]
    address=sys.argv[2]

    #creo socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #creo connessione
        s.connect((HOST,PORT))
        print("Connession established...")
        handleClient(s, address)
        print("Closing connection...")
        #chiudo la connessione
        s.close()

if __name__ == "__main__":
    main()