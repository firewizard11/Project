#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc > 3 || argc <= 2) {
        printf("The correct syntax is assignment9.exe FIRSTNAME LASTNAME");
    } else {
        printf("Hello, %s %s!", argv[1], argv[2]);
    }

    return 0;
}