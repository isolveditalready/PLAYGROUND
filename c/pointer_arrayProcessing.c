#include <stdio.h>

#define N 10


int main() {
    int a[N] =  { 1,2,3,4,5,6,7,8,9,10};
    int sum;
    int *p;

    sum = 0;
    for (p=&a[0]; p < &a[N]; p++) {
        sum += *p;
        printf("inside sum is %d", sum);
    }
    printf("why is this\n");
    printf("sum is %d", sum);
}