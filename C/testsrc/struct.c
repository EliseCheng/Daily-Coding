#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>

#define LEN 81
#define MAXTITL 40
#define MAXAUTL 40
#define MAXBKS 10

struct namect {
	char * fname;
	char * lname;
	int letters;
};

struct book {
	char title[MAXTITL];
	char author[MAXAUTL];
	float value;
};

typedef struct month {
	char * m_name;
	char *m_abbr; //3 words.
	int m_days;
	int m_no;
} MON;



void getinfo(struct namect *);
void makeinfo(struct namect *);
void showinfo(const struct namect *);
void cleanup(struct namect *);
void init_months(MON *);
void print_mon(MON *);

int main()
{
	//struct namect person;
	//getinfo(&person);
	//makeinfo(&person);
	MON months[12];
	init_months(months);
	FILE *fmon;
	if((fmon = fopen("mon.txt", "a")) == NULL)
	{
		exit(1);
	}

	int i;
	for(i = 0; i < 12; i++)
	{
		print_mon(&months[i]);
		if(fprintf(fmon, "%s:%s:%d:%d\n", months[i].m_name, months[i].m_abbr, months[i].m_days, months[i].m_no) < 0)
		{
			printf("%s", strerror(errno));
		}
	}
	fclose(fmon);
/*	
	struct book library[MAXBKS];
	strcpy(library[0].title, "hello world");
	strcpy(library[0].author, "alice");
	library[0].value = 11.0;
	FILE *fp;
	int size = sizeof(struct book);
	if((fp = fopen("book.txt", "a+b")) == NULL)
	{
		exit(1);
	}
	rewind(fp);
	fwrite(&library[0], size, 1, fp);
	fclose(fp);	
*/	
	return 0;
}

void getinfo(struct namect * person)
{
	char temp[LEN];
	printf("Enter your first name:\n");
	//gets(temp);
	person->fname = (char *) malloc(strlen(temp) + 1);
	strcpy(person->fname, temp);
}

void init_months(MON * m)
{
	char *months[] = {"January", "February", "March", "April", "May", "June", 
										"July", "August", "September", "October", "November", "December"};
	char *mon_abbrs[] = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
	int i = 0;
	while(i < 12)
	{
		m[i].m_name = months[i];
		m[i].m_abbr = mon_abbrs[i];
		m[i].m_days = 30;
		m[i].m_no = 1;
		i++;
	}
}

void print_mon(MON * m)
{
	printf("%s:%s:%d:%d\n", m->m_name, m->m_abbr, m->m_days, m->m_no);
}
