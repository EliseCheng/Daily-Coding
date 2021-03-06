#include <stdio.h>
#include <stdlib.h>

#define MAX 255

void read_file();
void file_rw(FILE *fp_dest, char *file_name);

int main()
{
	char *src_files[3] = {"mon.txt", "te2", "tet3"};
	char *dest_file = "hello";
	FILE *fp_dest;
	int i;
	if ((fp_dest = fopen(dest_file, "a")) == NULL)
	{
		exit(1);
	}
	for (i = 0; i < 3; i++)
	{
		file_rw(fp_dest, src_files[i]);
	}
	//file_rw(dest_file, src_files);
	if (fclose(fp_dest) != 0)
	{
		fprintf(stderr, "Error closing file\n");
		exit(1);
	}
	return 0;
}

/*
void file_rw(char *dest_file, char **src_files)
{
	//printf("test...\n");
	int i;
	FILE *fp;
	for (i = 0; i < 3; i++)
	{
		read_file(src_files[i]);
	}
}*/

void file_rw(FILE *fp_dest, char *fname)
{
	FILE *fp;
	char words[MAX];
	if ((fp = fopen(fname, "r")) == NULL)
	{
		fprintf(stderr, "%s can not be opened.", fname);
		exit(1);
	}
	//while(fscanf(fp, "%s", words) != EOF)
	while (fgets(words, 255, fp) != NULL)
	{
		//puts(words);//, stdout);
		//printf("%s", words);
		fputs(words, fp_dest);
	}
	if (fclose(fp) != 0)
	{
		fprintf(stderr, "Error closing file\n");
		exit(1);
	}
}
