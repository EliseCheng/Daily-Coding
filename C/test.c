#include <stdio.h>
void test()
{
	int a[]={};
	int i;
	for(i=0;i<10;i++)
	{
		a[i]=i;
	}
	printf("%d, %d, %d", sizeof(int), sizeof(char), sizeof(float));
	//return 0;
}

int main()
{
	//printf("%d, %d, %d", sizeof(int), sizeof(char), sizeof(float));
	int x = 10;
	x &= 10;
	char a;
	a = (01 & 1); //+ '0';
	printf("%d, %p\n", x, &a);
	return 0;
}
