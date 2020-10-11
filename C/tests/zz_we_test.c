//
/* Created by rock on 5/13/20.
*/

#include "common.h"
#include <stdio.h>
#include <unistd.h>

int vtest1(){
    int n1,n2,i,gcd;
    printf("输入两个整数:");
    scanf("%d %d", &n1, &n2);
    for (i = 1; i <= n1 && i <= n2; ++i) {
        if (n1 % i == 0 && n2 % i == 0) {
            gcd = i;
        }
    }
    printf("最大公约数:%d", gcd);

    for (int j = 0; j < 100; ++j) {
        int * result;
        sleep(10);
        result = (int *) malloc(2 * sizeof(int));
    }
    return gcd;
}

void vtest2(){

}


int main(int argc, char **argv)
{
    vtest1();
    return 0;
}