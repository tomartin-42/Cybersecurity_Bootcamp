#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/inotify.h>
#include "scaner.h"

static void	print_inotify(t_event aux)
{
	FILE	*fd;

	fd = fopen(TEMPORAL_LINUX_LOG_FILE, "a");
	//fprintf(fd, "%d - %d - %d - %d - %s\n", aux.wd, aux.mask, aux.cookie, aux.len, aux.path);
	fprintf(fd, "%d - %d \n", aux.wd, aux.len);
	fclose(fd);
}

static void read_events(t_file *scan_f)
{
	t_event	event;
	int		aux;

	aux = scan_f[0].n_arg;
	while(1)
	{
		while(aux >= 0)
		{
			read(scan_f[aux].watch_fd, &event, sizeof(t_event) + event.len);
			print_inotify(event);
			aux--;
		}
		sleep(5);
	}
}

static void	init_files_watch_to_read(t_file *scan_f, int i_fd)
{
	int	aux;

	aux = scan_f[0].n_arg;
	while(aux >= 0)
	{
		scan_f[aux].watch_fd = inotify_add_watch(i_fd, scan_f[aux].file, IN_ACCESS);
		aux--;
	}
	read_events(scan_f);
}

void	*(rutine_inotify(void *arg))
{
	t_file	*scan_f;
	int		i_fd;

	i_fd = inotify_init();
	scan_f = arg;
	init_files_watch_to_read(scan_f, i_fd);
}

void	init_inotify_rutine(t_file *scan_f, pthread_t thread)
{
	pthread_create(&thread, NULL, rutine_inotify, scan_f);
}
