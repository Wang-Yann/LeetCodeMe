#include "leetcode_functions.h"


bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }
    int copy = x;
    long reversed = 0;
    while (copy) {
        reversed = 10 * reversed + copy % 10;
        copy /= 10;
    }
    return reversed == x;

}
