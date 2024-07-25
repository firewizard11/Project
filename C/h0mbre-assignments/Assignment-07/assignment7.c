#include <stdio.h>
#include <math.h>

int main() {

    //Variables
    int a, b, c;
    float posResult, negResult;

    //User Input
    printf("Enter the value of variable 'A': ");
    scanf("%d", &a);
    printf("Enter the value of variable 'B': ");
    scanf("%d", &b);
    printf("Enter the value of variabe 'C': ");
    scanf("%d", &c);

    //Calculations
    posResult = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
    negResult = (-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);

    //Output + Check if correct (ax^2 + bx + c = 0)
    if (((a * pow(posResult, 2)) + (b * posResult) + c) == 0) {
        printf("The solution using the '+' operator is: %f\n", posResult);
    } else {
        printf("The solution using the '+' operator is: %f, but you might want to double-check that...\n", posResult);
    }

    if (((a * pow(negResult, 2)) + (b * negResult) + c) == 0) {
        printf("The solution using the '-' operator is: %f", negResult);
    } else {
        printf("The solution using the '-' operator is: %f, but you might want to double-check that...\n", negResult);
    } 

    return 0;
}