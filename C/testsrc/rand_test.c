#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define EVEN_GT(X, Y) (((X) % 2 == 0 && (X) > (Y)) ? 1 : 0)

int main()
{
	int r, i;
	srand((unsigned int)time(0));
/*for (i = 0; i < 10; i++)
	{
		r = rand()%100;
		printf("%d\n", r);
	}
*/
	double rd = (double) rand() / ((double) rand() + 0.1);
	printf("%0.4f\n", rd);	
	return 0;
}
