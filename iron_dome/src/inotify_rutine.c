#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/inotify.h>
#include "scaner.h"

static void	print_inotify(int len, char *buff)
{
	FILE	*fd;
	int		i;
	t_event *event;

	i = 0;
	fd = fopen(TEMPORAL_LINUX_LOG_FILE, "a");
	while(i < len)
	{
		event = (t_event *) &(buff[i]);
		fprintf(fd, "%d - %d - %d - %d - %s\n", 
				event->wd, event->mask, event->cookie, event->len, event->path);
		//fprintf(fd, "name = %s \n", event.name);
		i += EVENT_SIZE + event->len;
	}
	fclose(fd);
}

static void read_events(t_file *scan_f)
{
	char	buff[BUFF_LEN];
	int		len;
	int		i;
	int		aux;

	aux = scan_f[0].n_arg;
	while(1)
	{
		while(aux >= 0)
		{
			len = read(scan_f[aux].watch_fd, buff, BUFF_LEN);
			printf("-- %d * %d --\n", sizeof(buff), len);
			print_inotify(len, buff);
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
		scan_f[aux].watch_fd = inotify_add_watch(i_fd, scan_f[aux].file, IN_ACCESS | IN_OPEN);
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
