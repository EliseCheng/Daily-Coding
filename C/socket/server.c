#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 1987
#define BACKLOG 10

int main()
{
	int sockfd;
	int new_sockfd;
	socklen_t size_addr;
	struct sockaddr_in my_addr;
	struct sockaddr_in remote_addr;

	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
	{
		printf("Failed to initialize socket file description: %s\n", strerror(errno));
		exit(1);
	}
	
	my_addr.sin_family = AF_INET;
	my_addr.sin_port = htons(PORT);
	my_addr.sin_addr.s_addr = INADDR_ANY;
	memset(&(my_addr.sin_zero), 0, 8);

	if(bind(sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr)) == -1)
	{
		printf("Failed to bind my address : %s\n", strerror(errno));
		exit(1);
	}	
	if(listen(sockfd, BACKLOG) == -1)
	{
		printf("Error for listen: %s", strerror(errno));
		exit(1);
	}
	
	size_addr = sizeof(struct sockaddr_in);
	while(1)
	{
		printf("Start to accept...\n");
		//new_sockfd = accept(sockfd, (struct sockaddr*)&remote_addr, (socklen_t*)sizeof(struct sockaddr));
		new_sockfd = accept(sockfd, (struct sockaddr*)&remote_addr, &size_addr);
		if(new_sockfd == -1)
		{
			printf("accept error.. %s\n", strerror(errno));
			continue;
		}
	
		char *msg="Hello, this is server...";
		int result;
		printf("Send message to client.\n");
		result = send(new_sockfd, msg, strlen(msg), 0);
		if(result == -1)
		{
			printf("send error.. %s", strerror(errno));
			exit(1);
		}

	}
	
	close(new_sockfd);
	close(sockfd);
	return 0;
}
