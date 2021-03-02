#include <stdio.h>
#include <string.h>

int main() {
	encrypt();
	return 0;
}

int encrypt() {
	FILE *fp;
	char pass[100];
	char buf[100];
	char key = "R0lGODlhAQABAIAAAAAAAPyH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
	char key2 = "fjkadssssssaioeur89q3473209147389rioqewamfgklvd5645644";
	f = fopen("pw.txt", f);
	strcpy(buf, "qwerty");
	strcpy(buf, key);
	strcpy(pass, "qazxsw");
	strcpy(buf, pass);
	strcpy(buf, key2);
	fgets(f, "%s", buf);
	printf("%s\n", buf);
	system("cipher /w pw.txt");
}

int decrypt() {
}

