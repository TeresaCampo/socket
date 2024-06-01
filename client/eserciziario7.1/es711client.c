#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

// funzione error da usare sempre
void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    // controllo parametri:nome server e numero di porta come parametro
    struct hostent *server;
    int portno, sockfd;

    if (argc != 2)
    {
        error("ERROR: the function accept 1 parameter(server name)");
        exit(0);
    }
    server = gethostbyname(argv[1]);
    if (server == NULL)
    {
        error("ERROR: invalid host");
    }
    portno = 2525;
    sockfd = socket(AF_INET, SOCK_STREAM, 0); // AF_INET--> IPv4, SOCK_STREAM-->TCP
    if (sockfd < 0)
    {
        error("ERROR: failed to open the socket");
    }
    // posso iniziare l'esercizio

    // preparo info sul server al quale mi devo connettere a avvio connessione
    struct sockaddr_in server_address;
    bzero((char *)&server_address, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(portno);
    bcopy((char *)server->h_addr, (char *)&server_address.sin_addr.s_addr, server->h_length);

    // provo a connettermi al server
    if (connect(sockfd, (const struct sockaddr *)&server_address, sizeof(server_address)) < 0)
    {
        error("ERROR: failed to create connection with the server");
    }

    printf("Connection established...\n");
    char buffer[255];
    int n = read(sockfd, buffer, sizeof(buffer));
    printf("%s\n", buffer);

    printf("Closing conection...\n");
    return 0;
}