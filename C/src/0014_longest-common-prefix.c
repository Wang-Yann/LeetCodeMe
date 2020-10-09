//
/* Created by rock on 6/15/20.
*/

#include "leetcode_functions.h"

//char tmp[100] = {""};

char *longestCommonPrefix(char **strs, int strsSize) {
    if (strsSize == 0) {
        return "";
    }
    for (int i = 0; i < strlen(strs[0]); i++) {
        for (int j = 1; j < strsSize; j++) {
            if (strs[0][i] != strs[j][i]) {
//                printf("i:%d\n", i);
//                strncpy(tmp + i, strs[0], i - 1);
                strs[0][i] = '\0';
                break;
            }

        }
//        ans[i] = '\0';

    }
    return strs[0];


}