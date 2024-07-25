#include <stdio.h>

int main() {

    //Variables
    int numerator, denominator;

    //User Input
    printf("Enter a numerator: ");
    scanf("%d", &numerator);
    printf("Enter a denominator: ");
    scanf("%d", &denominator);

    //Check if remainder present and Output
    if (numerator % denominator == 0) {
        printf("There is NOT a remainder!");
    } else {
        printf("There is a remainder!");
    }

    return 0;
}