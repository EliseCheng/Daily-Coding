#include <stdio.h>
#include <string.h>
int main()
{
	char ch;
	char *fch;
	/*while ((ch = getchar()) != EOF)
	{
		putchar(ch);
	}
	fgets(fch, 3, stdin);
	char *fch_b = fch;
	while (*fch_b)
	{
		if (islower(*fch_b))
		{
			*fch_b = toupper(*fch_b);
		}
		fch_b++;
	}*/
	char *str;
	strcpy(str, "hello world");
	printf("%s\n", fch);
	return 0;
}
