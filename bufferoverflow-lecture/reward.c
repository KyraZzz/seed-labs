#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    char name[20];
    int reward;
    char payee[18];
    // addr(reward) - addr(payee) = -0x4
    // addr(payee) - addr(name) = -0x20

    srand(time(NULL)); /* seed the RNG */

    if (rand() % 2){
        reward = 5;
    }else {
        reward = 10;
    }

    printf("Your name?");
    gets(name);
    printf("Your sort code and bank account?");
    gets(payee);

    printf("Congratulations, %s! Send you %d GBP to %s.\n", name, reward, payee);
    return 0;
}