//
/* Created by rock on 6/2/20.
*/
#include "leetcode_functions.h"
//char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

int translateNum(int num) {
    char s[33];
    sprintf(s, "%d", num);
    int a = 1;
    int b = 1;
    int i = 2;
    int len = strlen(s);
    while (i <= len) {
//        printf("%d,%d\n", a, b);
        int tmp_a = a;
        char tmp[3]={""};
        strncpy(tmp, s+i-2, 2);
//        printf("tmp:%s\n", tmp);
//        printf("CMP:%d,%d\n", strcmp(tmp, "10") >= 0, strcmp(tmp, "25") <= 0);
        if (strcmp(tmp, "10") >= 0 && strcmp(tmp, "25") <= 0) {
            a = a + b;
        }
        b = tmp_a;
        i++;
    }
    return a;

}