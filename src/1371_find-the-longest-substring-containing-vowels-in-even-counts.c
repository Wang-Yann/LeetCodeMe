//
/* Created by rock on 5/20/20.
*/

#include "leetcode_functions.h"
int findTheLongestSubstring(char *s) {
    int dp[32];
    for (int i = 0; i < 32; ++i) {
        dp[i] = INT_MIN;
    }
    dp[0] = -1;
    int pattern = 0;
    int res = 0;
    int length = strlen(s);
    for (int i = 0; i < length; ++i) {
        switch (s[i]) {
            case 'a':
                pattern ^= (1 << 0);
                break;
            case 'e':
                pattern ^= (1 << 1);
                break;
            case 'i':
                pattern ^= (1 << 2);
                break;
            case 'o':
                pattern ^= (1 << 3);
                break;
            case 'u':
                pattern ^= (1 << 4);
                break;
            default:
                break;
        }
        if (dp[pattern] != INT_MIN) {
            res = max(res, i - dp[pattern]);
        } else {
            dp[pattern] = i;
        }


    }
    return res;

}