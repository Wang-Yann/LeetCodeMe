//
/* Created by rock on 4/30/20.
*/
#include "leetcode_functions.h"

int strStr(char * haystack, char * needle){
    int i;
    int len_l = strlen(needle);
    int len_h = strlen(haystack);

    if (haystack == NULL || needle == NULL || len_l == 0) {
        return 0;
    }

    for (i = 0; i <= len_h-len_l; ++i) {
        if (memcmp(&haystack[i], needle, len_l)==0) {
            return i;
        }

    }
    return -1;



}

//int main(){
//
//    const char* haystack = "hello";
//    const char*  needle =  "ll";
//    int res = strStr(haystack, needle);
//    printf("Res:%d", res);
//
//}