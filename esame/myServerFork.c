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
unsigned int ip2uint(char *ip)
{
    unsigned int ip3, ip2, ip1, ip0;
    sscanf(ip, "%d.%d.%d.%d", &ip3, &ip2, &ip1, &ip0);
    return (ip3 << 24) + (ip2 << 16) + (ip1 << 8) + ip0;
}
void handleClient(int client_sockfd)
{
    // leggo i dati
    char buffer[256];
    bzero(buffer, sizeof(buffer));
    int nr = read(client_sockfd, buffer, sizeof(buffer));
    // prelevo i valori
    int length = buffer[1];
    char ip[length];
    strncpy(ip, buffer + 2, length);
    unsigned ipv4 = ip2uint(ip);
    // preparo la risposta
    char response[7];
    bzero(response, sizeof(response));

    response[0] = 'R';
    response[1] = 4;
    unsigned int unsignedIpv4 = htonl(ipv4);
    response[2] = unsignedIpv4;
    response[3] = unsignedIpv4 >> 8;
    response[4] = unsignedIpv4 >> 16;
    response[5] = unsignedIpv4 >> 24;
    response[6] = 0;
    // invio risposta
    int nw = write(client_sockfd, response, sizeof(response));
}

int main(int argc, char *argv[])
{
    // controllo i parametri: accetta porta sulla quale ascoltare
    int portno, welcoming_sockfd;
    if (argc > 1)
    {
        error("ERROR: the function doesn't accept parameters");
    }
    portno = 1025;
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
    while (1)
    {
        client_sockfd = accept(welcoming_sockfd, (struct sockaddr *)&client_address, &client_len);
        if (client_sockfd < 0)
        {
            error("ERROR: failed to accept connection");
        }
        // fai cose
        int pid = fork();
        if (pid < 0)
        {
            error("ERROR: failed to create child process");
        }
        if (pid == 0)
        {
            printf("Connection established...\n");
            handleClient(client_sockfd);

            printf("Closing conection...\n");
            return 0;
        }
    }
    return 0;
}