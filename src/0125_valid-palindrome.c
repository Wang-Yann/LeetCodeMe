//
/* Created by rock on 6/19/20.
*/

#include "leetcode_functions.h"

bool isPalindrome1(char *s) {
    int len = strlen(s);
    int l = 0;
    int r = len - 1;
    while (l < r) {
        while (l < r && !isalpha(s[l]) && !isdigit(s[l])) {
            l++;
        }
        while (l < r && !isalpha(s[r]) && !isdigit(s[r])) {
            r--;
        }
        if (tolower(s[r]) != tolower(s[l])) {
            return false;
        }
        l++;
        r--;
    }
    return true;


}