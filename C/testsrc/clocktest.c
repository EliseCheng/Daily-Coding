#include <stdio.h>
#include <time.h>
void timeout(int times);
int main()
{
	struct tm *ptm;
	time_t t;
	time(&t);
	ptm = localtime(&t);
	char *time = asctime(ptm);
	ptm->tm_year += 1900;
	ptm->tm_mon++;
	//printf("%04d-%02d\n", ptm->tm_year, ptm->tm_mon);
	printf("%s\n", time);
	//timeout(3);

	return 0;
}

void timeout(int times)
{
	double sec = 0;
	clock_t c;
	while(sec < times)
	{
		c = clock();
		sec = c/CLOCKS_PER_SEC;
	}
	printf("%f\n", sec);
}
