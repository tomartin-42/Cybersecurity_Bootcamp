#include "scaner.h"
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include <time.h>
#include <fcntl.h>

static void	print_warning_entropy(t_file *scan_f, int i)
{
	time_t	t = time(NULL);
	struct	tm tm = *localtime(&t);
	FILE	*fd;

	fd = fopen(TEMPORAL_LOG_FILE, "w");
	fprintf(fd, "[%d-%02d-%02d %02d:%02d:%02d] WARNING ", tm.tm_year + 1900, 
		tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);
	fprintf(fd, "%s ", scan_f[i].file);
	fprintf(fd, "change entropy over %f ", ENTROPY_GATE);
	fprintf(fd, "entropy= %f -> ", scan_f[i].entropy);
	fprintf(fd, "new_entropy= %f\n", scan_f[i].new_entropy);
	fclose(fd);
}

void	*(rutine_entropy(void *arg))
{
	t_file	*scan_f;
	int		i;

	scan_f = arg;
	while(1)
	{
		i = 0;
		while(i < scan_f[0].n_arg)
		{
			scan_f[i].new_entropy = entropy(scan_f[i].file);
			if(scan_f[i].new_entropy > (scan_f[i].entropy * ENTROPY_GATE) + scan_f[i].entropy)
				//PRINTEA WARNING
				print_warning_entropy(scan_f, i);
			scan_f[i].entropy = scan_f[i].new_entropy;
			i++;
		}
		sleep(TIME_ENTROPY);
	}
}

void init_entropy_rutine(t_file *scan_f)
{
	pthread_t	thread;
	
	pthread_join(thread, NULL);
	pthread_create(&thread,	NULL, rutine_entropy, scan_f);
}
