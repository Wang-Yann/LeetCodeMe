//
/* Created by rock on 5/13/20.
*/

#include "common.h"
#include "mystr.h"

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

void testMystr()
{
    char buf[20]="012345126";
    char buf2[10];

    replaceFirst(buf,"12","9999");
    printf("replaceFirst:%s/n",buf);
    strcpy(buf,"012345126");
    replace(buf,"12","9999");
    printf("replace:%s/n",buf);
    strcpy(buf,"01234560");
    substring(buf2,buf,2,5);
    printf("substring:%s/n",buf2);
    printf("charAt:%c/n",charAt(buf,4));
    printf("indexOf:%d/n",indexOf(buf,"234"));
    printf("lastIndexOf:%d/n",lastIndexOf(buf,"0"));
    strcpy(buf,"    0123    ");
    ltrim(buf);
    printf("ltrim:||%s||/n",buf);
    strcpy(buf,"    0123     ");
    rtrim(buf);
    printf("rtrim:||%s||/n",buf);
    strcpy(buf,"    0123    ");
    trim(buf);
    printf("trim:||%s||/n",buf);
    strcpy(buf,"  ");
    trim(buf);
    printf("trim2:||%s||/n",buf);
}

int main()
{
//    testPrintArray();
//    testInitArray();
//    testPointArrayShow();
    char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
//    不需要把 null 字符放在字符串常量的末尾。C 编译器会在初始化数组时，自动把 '\0' 放在字符串的末尾
    char greeting1[] = "Hello";


    testMystr();
    return 0;
}