#define STACK_INT_SIZE 100
#define STACKINCREMENT 10

typedef struct {
	int *base;
	int *top;
	int stacksize;
} SqStack;


int initStack(SqStack *stack);
