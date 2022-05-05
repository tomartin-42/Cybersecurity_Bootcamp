#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include "scaner.h"

t_file *init_values(int argc, char **argv)
{
	t_file	*scan_f;
	int		i;
	
	scan_f = malloc(sizeof(t_file) * argc - 1);
	i = 0;
	while(i < argc - 1)
	{
		scan_f[i].n_arg = argc - 1;
		scan_f[i].file_numb = i;
		scan_f[i].file = strdup(argv[i + 1]);
		scan_f[i].n_read = 0;
		scan_f[i].entropy = entropy(scan_f[i].file);
		scan_f[i].new_entropy = 0;
		i++;
	}
	return scan_f;
}

int	main(int argc, char **argv)
{
	t_file		*scan_f;
	pthread_t	thread;

	if (argc == 1)
	{	
		dprintf(STDERR_FILENO, "[ERROR]"
			": No string argument provided! \n"
            "You must provide a path as argument\n");
        exit(1);
	}
	scan_f = init_values(argc, argv);
	pthread_join(thread, NULL);
	init_entropy_rutine(scan_f, thread);
	init_inotify_rutine(scan_f, thread);
	while (1)
		sleep (5);
	return 0;
}
