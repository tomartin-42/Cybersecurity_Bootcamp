#ifndef _SCANER_H
# define _SCANER_H

# define TIME_ENTROPY 30
# define ENTROPY_GATE 1.2
# define LOG_FILE "/var/log/irondome/irondome.log"

typedef struct s_file{
	int		n_arg;
	int		file_numb;
	char	*file;
	float	entropy;
	float	new_entropy;
} t_file;

float	entropy(char *file);

void	init_entropy_rutine(t_file *scan_f);
void	*rutinei_entropy(void *arg);
#endif

