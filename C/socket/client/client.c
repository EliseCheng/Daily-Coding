#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 1987
#define BUF_LEN 255

int main()
{
	int sockfd;
	struct sockaddr_in server_addr;
	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
	{
		printf("Failed to initialize socket file description: %s\n", strerror(errno));
		exit(1);
	}

	memset(&server_addr, 0, sizeof(struct sockaddr_in));
	server_addr.sin_family = AF_INET;	
	server_addr.sin_port = htons(PORT);
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	//inet_aton("127.0.0.1", &server_addr.sin_addr);
	
	printf("Start to connect to server..\n");
	if(connect(sockfd, (struct sockaddr*)&server_addr, sizeof(struct sockaddr)) == -1)
	{
		printf("connection error: %s\n", strerror(errno));
		exit(1);
	}
	
	char buf[BUF_LEN];
	recv(sockfd, buf, BUF_LEN, 0);
	printf("client: rev -- %s\n", buf);

	close(sockfd);
	
	
	return 0;
}
