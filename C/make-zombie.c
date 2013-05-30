#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main ()
{
	pid_t child_pid;
	/* Create a child process. */
	child_pid = fork ();
	if (child_pid > 0) 
	{
		/* This is the parent process. Sleep for a minute. */
		printf("child pid : %d\n", child_pid);
		sleep (60);
	}
	else 
	{
		printf("parent pid : %d\n", getppid());
		/* This is the child process. Exit immediately. */
		exit (0);
	}
	return 0;
}
