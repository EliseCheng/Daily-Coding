#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
	struct tm *ptm;
	time_t now;
	time(&now);
	ptm = localtime(&now);
	int year, month, day;
/*	
	union mon{
		char *m_full;
		char *m_abbr;
		int m_no;
	};
*/
	printf("Please input the date.\n year:");
	//scanf("%d", &year);
	printf("month:");
	//scanf("%d", &month);
	printf("day:");
	//scanf("%d", &day);
	//fgets()
	printf("%d-%d-%d\n", year, month, day);
	ptm->tm_year = 2013 - 1900;
	ptm->tm_mon = 4;//month - 1;
	ptm->tm_mday = 20;

	time_t date = mktime(ptm);
	double diff = difftime(now, date);
	int days = (int)(diff/60/60/24);
	printf("%d\n", days);
	
	return 0;
}
