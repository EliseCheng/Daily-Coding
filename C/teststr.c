#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void replace_blanks(const char* src, char* dest);
int main()
{
	char str[255];
	char dest[255];
	while(1)
	{
		printf("input your string('q' for quit):\n");
		gets(str);		
		if(str[0] == 'q')
		{
			printf("exit...\n");
			exit(0);
		}
		replace_blanks(str,dest);		
		printf("%s\n", str);
	}
	return 0;
}

void replace_blanks(const char* src, char *dest)
{
	while(*src++ != '\0')
	{
		if(*src == ' ')
		{
			
		}
	}
}
