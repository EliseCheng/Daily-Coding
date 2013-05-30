#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
int main()
{
	FILE *fp;
	if((fp=fopen("mo.txt", "r")) == NULL)
	{
		exit(1);
	}

	int a;
	char *b; 
	char *c;
	fscanf(fp, "%d %s %s", &a, b, c);
	printf("%s", strerror(errno));
	printf("%d %s %s\n", a, b, c);
	fclose(fp);
	return 0;
}
