#include <stdio.h>
#include "array.h"
int main()
{
	int arr[4]={6, 2, 3, 4};
	ELE *arr_a=cp_arr(arr+1, 3);
	print_array(arr_a);
	return 0;
}
