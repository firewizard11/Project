#include <stdio.h>

int main() {

    //Variable
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(array);
    int i;

    //Output
    printf("The array has 10 elements and takes up %d bytes of memory\n", size);
    printf("Here comes the elements of the array\n");

    for (i = 0; i < 10; i++) {
        printf("%d\n", array[i]);
    }

    return 0;
}