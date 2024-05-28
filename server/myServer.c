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
    // controllo i parametri: accetta porta sulla quale ascoltare
    int portno, welcoming_sockfd;
    if (argc != 2)
    {
        error("ERROR: the function accept 1 parameter(port number)");
    }
    portno = atoi(argv[1]);
    // posso iniziare l'esercizio

    // creo welcoming socket, faccio il bind con la porta e la metto in listening
    // creo la welcoming socket
    welcoming_sockfd = socket(AF_INET, SOCK_STREAM, 0); // AF_INET--> IPv4, SOCK_STREAM-->TCP
    if (welcoming_sockfd < 0)
    {
        error("ERROR: failed to create the welcoming socket");
    }

    // preparo struttura dati di indirizzo e porta con la quale fare binding
    struct sockaddr_in server_address;
    bzero((char *)&server_address, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = INADDR_ANY; // INADDR_ANY=0.0.0.0 cioè accetta connessioni con src qualsiasi IP publico
    server_address.sin_port = htons(portno);
    // faccio binding
    if (bind(welcoming_sockfd, (struct sockaddr *)&server_address, sizeof(server_address)) < 0)
    {
        error("ERROR: failed to bind the welcoming socket to the chosen port");
    }
    // faccio listen
    listen(welcoming_sockfd, 5);

    // accetto la connessioen di un client
    struct sockaddr_in client_address;
    int client_sockfd, client_len;
    client_len = sizeof(client_address);
    client_sockfd = accept(welcoming_sockfd, (struct sockaddr *)&client_address, &client_len);
    if (client_sockfd < 0)
    {
        error("ERROR: failed to accept connection");
    }
    printf("Connection established...\n");
    // fai cose
    printf("Closing conection...\n");
    return (0);
}