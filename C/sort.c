#include <stdio.h>
#include "array.h"
#define ASC 0
#define DES 1

void printIntArr(int *arr,int len);
void insert_sort(int *arr,int n);

int main()
{
	//int arr[]={5,2,3,1,4,6};
	int arr[]={1,3,5,7,2,4,6,8};
	merge(arr,0,3,7);
	//insert_sort(arr,6);
	printIntArr(arr,8);
	return 0;
}

void merge(int *arr, int p, int q, int r)
{
		int len_a=q-p+1;
		int len_b=r-q;
		int i=p;
		ELE *arr_a=cp_arr(arr,len_a);
		ELE *arr_b=cp_arr(arr+len_a,len_b);
		ELE *p_a=arr_a;
		ELE *p_b=arr_b;
		while(*p_a!=NULL && *p_b!=NULL)
		{
			if(p_a->num<p_b->num)
			{
				arr[i]=p_a->num;
				p_a=p_a->next;
			}else if(p_a->num==p_b->num)
			{
				arr[i]=p_a->num;
				p_a=p_a->next;
				arr[++i]=p_b->num;
				p_b=p_b->num;
			}else
			{
				arr[i]=p_b->num;
				p_b=p_b->next;
			}
			i++;
		}
		if(p_a==NULL)
		{
			while(p_b!=NULL)
			{
				arr[i++]=p_b->num;
			}
		}else
		{
			while(p_a!=NULL)
			{
				arr[i++]==p_a->num;
			}
		}
		
}

void merge_sort()
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
