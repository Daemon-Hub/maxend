// #include <stdio.h>

int main(void)
{
	system("git init");
	system("git add .");
	system("git commit -m \"init\"");
	system("git branch -M main");
	system("git remote add origin https://github.com/Daemon-Hub/maxend.git");
	system("git push -u origin main");
	return 0;
}