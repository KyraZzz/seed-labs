#include <stdio.h>
#include <stdlib.h>

extern char **environ; // environ already defined somewhere
int main(){
    int i = 0;
    while (environ[i] != NULL){
        printf("%s\n",environ[i]);
        i++;
    }
}