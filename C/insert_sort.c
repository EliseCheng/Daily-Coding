#include <stdio.h>

#define ASC 0
#define DES 1

void printIntArr(int *arr,int len);
void insert_sort(int *arr,int n);

int main()
{
	int arr[]={5,2,3,1,4,6};
	insert_sort(arr,6);
	printIntArr(arr,6);
	return 0;
}

void merge_sort(int *arr)
{
	
}

void insert_sort(int *arr,int n)
{
	int i=0,j=1;
	int key=0;
	for(;j<n;j++)
	{
		key=arr[j];
		i=j-1;
		//移动的位置相对于i
		while(i>=0 && key<arr[i])
		{
			arr[i+1]=arr[i];
			i=i-1;
		}
		arr[i+1]=key;
	}
}
void printIntArr(int *arr,int len)
{
	int i=0;
	for(i=0;i<len;i++)
	{
		printf("%d\n",arr[i]);
	}
}
