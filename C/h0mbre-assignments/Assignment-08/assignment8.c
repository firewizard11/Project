#include <stdio.h>

int main() {

    //Variables
    int userInput;

    //User Input
    printf("Enter a number between 1 and 500: ");
    scanf("%d", &userInput);

    //Checks + Output
    if (userInput >= 1 && userInput <= 100) {
        printf("Your number is between 1 and 100!");
    } else if (userInput > 100 && userInput <= 200) {
        printf("Your number is between 101 and 200!");
    } else if (userInput > 200 && userInput <= 300) {
        printf("Your number is between 201 and 300!");
    } else if (userInput > 300 && userInput <= 400) {
        printf("Your number is between 301 and 400!");
    } else if (userInput > 400 && userInput <= 500) {
        printf("Your number is between 401 and 500!");
    } else {
        printf("Your number is not in any of our ranges!");
    }

    return 0;
}