#include <stdio.h>
#include <stdlib.h>
#include "array.h"

ELE* create_element(int num)
{
	ELE *ele=malloc(sizeof(ELE));
	ele->num=num;
	ele->next=NULL;
	return ele;
}

//for testing
ELE* create_array(int len)
{
	int i=0;
	ELE *arr=create_element(i++);
	ELE *p=arr;	
	while(i<len)
	{
		ELE *q=create_element(i);
		p->next=q;
		p=q;
		i++;
	}
	return arr;
}


ELE* cp_arr(int *src_arr,  int len)
{
	int i=0;
	ELE *dst_arr=create_element(src_arr[0]);
	i++;
	ELE *p=dst_arr;
	
	while(i<len)
	{
		ELE *q=create_element(src_arr[i]);
		p->next=q;
		p=q;
		i++;
	}
	return dst_arr;
}

void print_array(ELE *ele)
{
	while(ele!=NULL)
	{
		printf("%d\n", ele->num);
		ele=ele->next;
	}
}

void free_array(ELE *ele)
{
	while(ele!=NULL)
	{
		ELE *p=ele;
		ele=ele->next;
		free(p);
	}
}

/*
int main()
{
	ELE *ele=create_array(15);
	print_array(ele);
	free_array(ele);
	return 0;
}
*/
