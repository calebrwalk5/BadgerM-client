#include <stdio.h>
#include <stdlib.h>
/* 
 * Indev 0.1
*/

char path[50];

int main() {
	printf("Enter The path of your GTA V addins folder in quotes: ");
	scanf("%s", path);
	system("copy /mods %s", path);
	startgame();
}

int startgame() {
	system("cd ../");
	system("cd injector");
	system("start injector.exe");
	system("start steam://rungameid/271590");
}
