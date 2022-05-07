#ifndef _SCANER_H
#include <pthread.h>
#include <stdint.h>

# define _SCANER_H
# define TIME_ENTROPY 10
# define ENTROPY_GATE 0.2
# define LOG_FILE "/var/log/irondome/irondome.log"
# define TEMPORAL_LOG_FILE "/Users/tomartin/sgoinfre/cybersec_bootcamp/iron_dome/log"
# define TEMPORAL_LINUX_LOG_FILE "/home/tommy/Cybersecurity_Bootcamp/iron_dome/log"
# define EVENT_SIZE	(sizeof(t_event))
# define BUFF_LEN	(1024 *(EVENT_SIZE + 16))

typedef struct s_file{
	int		n_arg;
	int		file_numb;
	char	*file;
	int		n_read;
	int		watch_fd;
	float	entropy;
	float	new_entropy;
} t_file;

typedef struct s_event{
    int			wd;
    uint32_t	mask;
    uint32_t	cookie;
    uint32_t	len;
    char			path[];
} t_event;

float	entropy(char *file);

void	init_entropy_rutine(t_file *scan_f, pthread_t thread);
void	*rutinei_entropy(void *arg);

void	init_inotify_rutine(t_file *scan_f, pthread_t thread);
void	*rutine_inotify(void *arg);
#endif

