#include <stdio.h>

int main() {

    //Variables
    int seconds, hours, minutes, remains;

    //User Input
    printf("Enter the amount of seconds: ");
    scanf("%d", &seconds);

    //Calculations
    hours = seconds / 3600;
    remains = seconds % 3600;

    minutes = remains / 60;
    remains %= 60;

    //Output
    printf("%d seconds is equal to %d hours, %d minutes, and %d seconds.", seconds, hours, minutes, remains);

    return 0;
}