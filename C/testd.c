#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string.h>

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

int main()
{
	pid_t pid,sid;

	FILE *file;

	char *str = "testing\n";
	if((file=fopen("testd.log", "a+")) == NULL)
	{
		printf("Open file failed.\n");		
		exit(EXIT_FAILURE);
	}

	pid = fork();

	if(pid < 0)
	{
		printf("Fork failed.\n");
		exit(EXIT_FAILURE);
	}
	if(pid > 0)
	{
		printf("Exit the parent process. ID: %d \n", pid);
		exit(EXIT_SUCCESS);
	}
	char *log = "I'm the child...";
	umask(0);
	//logs
	fwrite(log, sizeof(char), strlen(log), file);
	fflush(file);
	
	sid = setsid();
	if(sid < 0)
	{
		printf("Create session id failed.\n");
		exit(EXIT_FAILURE);
	}
	if(chdir("/") < 0)
	{
		exit(EXIT_FAILURE);
	}
	close(STDIN_FILENO);
	close(STDOUT_FILENO);
	close(STDERR_FILENO);

	//main task
	
	while(1)
	{
		fwrite(str,sizeof(char),strlen(str),file);
		fflush(file);
		sleep(20);	
	}
	fclose(file);
	return 0;
}
