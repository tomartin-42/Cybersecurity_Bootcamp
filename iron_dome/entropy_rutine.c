#include "scaner.h"
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>

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
			printf("HOLA1\n");
			scan_f[i].new_entropy = entropy(scan_f[i].file);
			printf("old %f\n new %f\n file %s",scan_f[i].entropy, scan_f[i].new_entropy, scan_f[i].file);
			if(scan_f[i].new_entropy * ENTROPY_GATE > scan_f[i].entropy)
				//PRINTEA WARNING
				printf("WARNING");
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
