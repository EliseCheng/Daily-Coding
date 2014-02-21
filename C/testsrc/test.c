#include <stdio.h>
#include <stdlib.h>
void prime();
void read();
int main(int argc, char *argv[])
{
/*
	int i;
	char str[100] = "hello world";

	for (i = 0; i < 3; i++)
	{
		str[i] = 'k';
	}
*/
/*
	char **p;
	p = (char **)malloc(sizeof(char *) * 3);
	p[0] = str;
	p[1] = str;
	i = (int)sizeof(p)/sizeof(char *);
	//p[0] = str;
	printf("%d\n", i);
	free(p);
	char *pp="ab";
	printf("%d\n", sizeof(*pp));
*/
	//prime();
	read();
	return 0;
} 
void prime()
{
	int i, j;
	for (i = 2; i < 1000; i++)
	{
		for(j = 2; j <= i/2;)
		{
			if(i%j == 0) break;
			else j++;
		}
		if(j > i/2) printf("%d\n", i);
	}
}

void read()
{
	double arr[10];
	int i = 0;
	char buf[255];
	
	while (fgets(buf, 255, stdin))
	{	
		//if (buf[0] == 'q') return;
		arr[i] = atof(buf);	
		printf("%f\n", arr[i]);
		i++;
	}
	puts("break from while.");
	int n;
	scanf("%d", &n);
}
