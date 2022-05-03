/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   entropy.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tomartin <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/05/01 15:23:27 by tomartin          #+#    #+#             */
/*   Updated: 2022/05/02 13:06:51 by tomartin         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <math.h>
#include "scaner.h"

static void	init_table(int *table)
{
	int	i;

	i = 0;
	while (i < 257)
		table[i++] = 0;
}

//leng is i and add table[256] and count number of bytes
static void	load_bytes_to_file(int fd, int *table)
{
	unsigned char	buff;
	int				i;

	i = 0;
	while (read(fd, &buff, 1))
	{
		table[buff]++;	
		i++;
	}
	table[256] = i;
	close(fd);
}

static float	calc_entropy(int *table)
{
	int 	i;
	float	entropy;
	float	aux;
	float	log256;

	i = 0;
	entropy = 0;
	log256 = log2(256);
	while (i < 256)	
	{
		if(table[i] == 0)
			;
		else
		{
			aux = 1.0 * table[i] / table[256];
			entropy -= aux * (log2(aux) / log256);
		}
		i++;
	}
	return entropy;
}	

float	entropy(char *file)
{
	int	table[257];
	int	fd;
	float entropy;

	entropy = 0;
	init_table(table);
	fd = open(file, O_RDONLY);
	if (fd > 0)
	{
		load_bytes_to_file(fd, table);
		entropy = calc_entropy(table);
	}
	printf("%f\n", entropy);
	return entropy * 100;
}


