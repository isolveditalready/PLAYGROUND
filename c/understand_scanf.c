#include <stdio.h>

int main(){
    char ch;
    do {
        scanf("%c", &ch);
        printf("c is %c", ch);
    } while (ch != '\n');
}