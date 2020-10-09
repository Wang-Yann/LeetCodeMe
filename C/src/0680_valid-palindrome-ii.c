//
/* Created by rock on 5/19/20.
*/
#include "leetcode_functions.h"

bool valid(char *s, int l, int r) {
    while (l < r ) {
        if (s[l] != s[r]) {
            return false;
        }
        l++;
        r--;
    }
    return true;
}


bool validPalindrome(char *s) {
    int l = 0;
    int r = strlen(s)-1;
    while (l < r) {
        if (s[l] != s[r]) {
            return valid(s, l, r - 1) || valid(s, l + 1, r);
        }
        l++;
        r--;
    }
    return true;


}