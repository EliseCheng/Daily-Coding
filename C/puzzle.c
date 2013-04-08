#include <stdio.h>

void printIntArr(int *arr)
{
	int length=sizeof(arr)/sizeof(int);
	printf("length is %d\n",length); //为什么输出的结果是1，不是6？
}

int main()
{
	int arr[]={5,2,3,1,4,6};
	printIntArr(arr);
}
