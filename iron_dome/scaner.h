#ifndef _SCANER_H
# define _SCANER_H

# define TIME_ENTROPY 10
# define ENTROPY_GATE 0.2
# define LOG_FILE "/var/log/irondome/irondome.log"
# define TEMPORAL_LOG_FILE "/Users/tomartin/sgoinfre/cybersec_bootcamp/iron_dome/log"
# define TEMPORAL_LINUX_LOG_FILE "/home/tommy/Cybersecurity_Bootcamp/iron_dome/log"


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

