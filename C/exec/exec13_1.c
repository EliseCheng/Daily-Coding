#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "exec13_1.h"

int main(int argc, char *argv[])
{
//exec13.1-2
	char chs[255];
	memset(chs, 0, 255);

	int i, num;
/*
	if (argc < 2)
	{
		printf("Please provide the number you want to enter.\n");
		exit(0);
	}
	num = atoi(argv[1]);
	printf("You want to enter %d characters.\n", num);
	read_chars(chs, num);
	for(i = 0; i < num; i++)
	{
		printf("%c", chs[i]);
	}
*/
//exec13.3
/*
	read_1th_word(chs);
	//printf("%s\n", chs);
	for (i = 0; i < strlen(chs); i++)
	{
		printf("%c\n", chs[i]);
	}
*/
/*
	
	ch = mystrchr("hello world", 'o');
	if (ch)
		printf("%p\n", ch);



	char s1[3];
	memset(s1, 0, 3);
	char *s2 = "hello world...";
	mystrncpy(s1, s2, 6);
	printf("%s\n", s1);
*/
/*
	
	ch = string_in("hello", "ho");
	if (ch)
		printf("%c\n", *ch);
	else
		printf("NULL\n");
*/
	char ch[255] = "see you latter";
	//inverse_str(ch);
	char **p = split(ch, ' ');
	i = 0;
	while(p[i] != NULL)
	{
		printf("%s\n", p[i]);
		i++;
	}
	char chr[255];
	memset(chr, 0, 255);
	sprintf(chr, "%s %s %s", p[2], p[1], p[0]);
	printf("%s\n", chr);
	return 0;
}

void read_chars(char *chars, int num)
{
	int i;
	char ch;
	for (i = 0; i < num; i++)
	{
		ch = getchar();
		switch(ch)
		{
			case '\r':
			case '\t':
			case '\n':
			case ' ':
				printf("Got %d, we return!\n", ch);
				return;
			default:
				chars[i] = ch;
		}
	}
}

void read_1th_word(char *words)
{
	scanf("%s", words);
}


char* mystrchr(char *chars, char target)
{
	int i;
	for (i = 0; i < strlen(chars); i++)
	{
		if (target == chars[i])
		{
			return chars+i;
		}
	}
	return NULL;
}


void mystrncpy(char *s1, char *s2, int n)
{
	int i;
	for (i = 0; i < n && s2[i] != 0; i++)
	{
		s1[i] = s2[i];	
	}

}
//hello lo
char* string_in(char *s1, char *s2)
{
	int n = strlen(s2);
	int i;
	for (i = 0; s1[i] != '\0'; i++)
	{
		if (strncmp((s1 + i), s2, n) == 0)
			return s1+i;
	}

	return NULL;
}

void inverse_str(char *str)
{
	int n = strlen(str);
	int i;
	char temp;
	for (i = 0; i < n/2; i++)
	{
		temp = str[i];
		str[i] = str[n - 1 - i];
		str[n -1 - i] = temp;
	}
}

char* inverse_words(char *str)
{
	return NULL;
		
}

char** split(char *str, char ch)
{
	int i = 0, count;
	char *temp = str;
	char **p;
	if((count = split_num(str, ch)) == 0)
	{
		*p = str; 
		return *p;
	}
	p = (char **)malloc(sizeof(char*) * (count+1));
	while(i < count)
	{
		p[i++] = str;
		int pos = ch_pos(str, ch);
		char *t = str + pos;
		str = str + pos +1;
		t[0] = '\0';
	}
	p[i] = NULL;
	return p;
}

int ch_pos(char *str, char ch)
{
	int i = 0;
	while(str[i] != '\0' && str[i] != ch)
	{
		i++;
	}
	if(str[i] == '\0')	return -1;
	
	return i;
}

int split_num(char *str, char ch)
{
	int i;
	int count = 0;
	for (i = 0; str[i] != '\0'; i++)
	{
		if(ch == str[i])
		{
			count++;
		}
	}
	return count+1;
}
