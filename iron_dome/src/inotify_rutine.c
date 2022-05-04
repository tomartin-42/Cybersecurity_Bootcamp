#include <pthread.h>
#include <sys/inotify.h>
#include "scaner.h"

static void	init_files_watch_to_read(t_file *scan_f, int i_fd)
{
	int	aux;

	aux = scan_f[0].n_arg;
	while(aux >= 0)
	{
		scan_f[aux].watch_fd = inotify_add_watch(i_fd, scan_f[aux].file, IN_ACCESS);
		aux++;
	}
}

void	*(rutine_inotify(void *arg))
{
	t_file	*scan_f;
	int		i_fd;

	i_fd = inotify_init();
	scan_f = arg;
	init_files_watch_to_read(scan_f, i_fd);
}

void	init_inotify_rutine(t_file *scan_f)
{
	pthread_t	thread;

	pthread_join(thread, NULL);
	pthread_create(&thread, NULL, rutine_inotify, scan_f);
}
