#include <string.h>
#include <io.h>
#include <stdio.h>

int main(int argc, char** argv)
{
	char	buff[8];
	strcpy(buff, argv[1]);
	//strcpy(buff, "AAAAAAAAAAAABBB\x41");
	printf(buff);
	return (0);
}