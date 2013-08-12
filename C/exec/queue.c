#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

int initStack(SqStack *s)
{
	s->base = (int *)malloc(sizeof(int) * STACK_INT_SIZE);
	s->top = s->base;
	s->stacksize = STACK_INT_SIZE;
	if(s->base == NULL)
		return -1;
	else
		return 0;
}

void main()
{
	SqStack *s;
	printf("%d\n", initStack(s));
	
}
