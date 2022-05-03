#ifndef _SCANER_H
# define _SCANER_H

typedef struct s_file{
	int		file_numb;
	char	*file;
	float	entropy;
	float	new_entropy;
} t_file;

float	entropy(char *file);

#endif

