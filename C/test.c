#include <stdio.h>
void test()
{
	int a[]={};
	int i;
	for(i=0;i<10;i++)
	{
		a[i]=i;
	}
	printf("%d",a[9]);
	//return 0;
}
