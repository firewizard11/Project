#include <stdio.h>

int main() {

    // Variables
    char first[30];
    char last[30];

    // User Input
    printf("Enter your first name: ");
    scanf("%s", first);
    printf("Enter your last name: ");
    scanf("%s", last);

    // Output
    printf("Hello %s %s!", first, last);

    return 0;
}