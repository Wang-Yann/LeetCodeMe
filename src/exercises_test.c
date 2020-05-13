//
/* Created by rock on 5/13/20.
*/

#include "common.h"

void testPrintArray(){
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    printf("%lu\n", sizeof(a[0]));
}

void testInitArray(){
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    int a1[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    int a2[3][4] = {{1, 2}, {5}, {9}};
    int a3[][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    int a4[2][4] = {0};

    int i;  //行循环变量
    int j;  //列循环变量
    for (i=0; i<3; ++i)
    {
        for (j=0; j<4; ++j)
        {
            printf("%-2d\x20", a2[i][j]);
        }
        printf("\n");
    }

}

void testPointArrayShow(){
    int tmp1[] = {1};
    int tmp2[] = {3,2};
    int *pairs[2] = {tmp1,tmp2};

    for (int  i=0; i<2; ++i)
    {
        for (int j=0; j<2; ++j)
        {
            printf("%-2d\t", *(pairs[i]+j));
        }
        printf("\n");
    }

}

int main(void)
{
//    testPrintArray();
//    testInitArray();
    testPointArrayShow();
    return 0;
}