#include <stdlib.h>
#include <string.h>
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
		scan_f[i].file_numb = i;
		scan_f[i].file = strdup(argv[i + 1]);
		scan_f[i].entropy = entropy(scan_f[i].file);
		scan_f[i].new_entropy = 0;
		i++;
	}
}

int	main(int argc, char **argv)
{
	if (argc == 1)
	{	
		dprintf(STDERR_FILENO, "[ERROR]"
			": No string argument provided! \n"
            "You must provide a path as argument\n");
        exit(1);
	}
	init_values(argc, argv);
	return 0;
}

