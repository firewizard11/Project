#include <stdio.h>
#define PIE 3.14

int main() {

    //Variables
    float radius;
    float area;

    //User Input
    printf("Enter the radius of your circle: ");
    scanf("%f", &radius);

    //Calculation
    area = PIE * (radius * radius);

    //Output
    printf("The area of your circle is %f", area);

    return 0;
}