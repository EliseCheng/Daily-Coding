#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 255
void average(int argc, char *argv[]);
void print_line(int argc, char *argv[]);
int main (int argc, char *argv[])
{
	
	//average(int argc, char *argv[]);
	print_line(argc, argv);
	return 0;
}

void average(int argc, char *argv[])
{
	float sum = 0;
	float num[MAX];
	int i = 0;
	char buf[MAX];
	FILE *fp;

	if (argc > 2)
	{
		puts("1 parameter at most");
		exit(1);
	}
	if (argc == 2)
	{
		if ((fp = fopen(argv[1], "rb")) == NULL)
		{
			fprintf(stderr, "Error in opening file %s.\n", argv[1]);
			exit(1);
		}
	}
	else 
	{
		fp = stdin;
		fprintf(stdout, "Please enter float numbers, break with [ctrl+D].\n");
	}
	//memset(buf, 0, MAX);
	
	while (fgets(buf, 255, fp))
	{
		puts(buf);
		num[i] = atof(buf);
		printf("%0.4f\n", num[i]);
		sum += num[i];
		i++;
	}
	printf("i = %d; aver = %0.4f\n", i, sum / i);
	fclose(fp);
}

void print_line(int argc, char *argv[])
{
	char ch;
	FILE *fp;
	char buf[MAX];
	if (argc != 3)
	{
		fprintf(stderr, "Please enter 2 parameters: character and file name.\n");
		exit(1);
	}
	if (strlen(argv[1]) > 1)
	{
		fprintf(stderr, "The 1st paramenter should be a character.\n");
		exit(1);
	}
	else ch = argv[1][0];
	if ((fp = fopen(argv[2], "r")) == NULL)
	{
		fprintf(stderr, "Error in opening file, please check file name is correct\n");
		exit(1);
	}
	while (fgets(buf, MAX, fp))
	{
		if (strchr(buf, ch))
		{
			puts(buf);
		}
	}
	fclose(fp);
}
