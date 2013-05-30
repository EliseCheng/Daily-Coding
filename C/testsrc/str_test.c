#include <stdio.h>
#include <string.h>
#include "str_test.h"

#define SIZE 255
#define LIM 5


int main()
{
	char strs[LIM][SIZE];
	char *pstr[LIM];
	int size = SIZE;
	int ct = 0;
	printf("Input %d strings:\n", LIM);
	while (ct < LIM && fgets(strs[ct], SIZE, stdin) != NULL) // && strs[ct][0] != '\0'
	{
		char *temp;
		temp = strchr(strs[ct], '\n');
		if(temp) *temp = '\0';
		pstr[ct] = strs[ct];
		ct++;
	}
	printf("===============\n");
	strsort(pstr, LIM);
	int i;
	for (i = 0; i < LIM; i++)
	{
		printf("%s\n", pstr[i]);
	}
	return 0;
}

void strsort(char *pstr[], int num)
{
	int i, j=1;
	char *key;
	for(; j < num; j++)
	{
		key = pstr[j];
		i = j-1;
		while (i>=0 && strcmp(key, pstr[i]) < 0)
		{
			pstr[i+1] = pstr[i];
			i--;
		}
		pstr[i+1] = key;
	}
	
}
