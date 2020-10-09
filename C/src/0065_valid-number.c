//
/* Created by rock on 5/4/20.
*/

#include "leetcode_functions.h"

bool isNumber(char *s) {
    bool bIsNum = false;
    while (isspace(*s)) {
        s++;
    }
    if (*s == '+' || *s == '-') {
        s++;
    }
    while (isdigit(*s)) {
        bIsNum = true;
        s++;
    }
    if ('.' == *s) {
        s++;
    }
    while (isdigit(*s)) {
        bIsNum = true;
        s++;
    }
    if (bIsNum && *s == 'e') {
        s++;
        bIsNum = false;
        if ('+' == *s || '-' == *s) // 幂次方允许出现一个符号
        {
            s++;
        }

        while (isdigit(*s)) // 幂次方部分
        {
            s++;
            bIsNum = true;
        }


    }
    while (isspace(*s)) {
        s++;
    }
    return '\0' == *s && bIsNum;


}