#include "leetcode_functions.h"


#define isOverLength 0

int reverse(int x){
    long lret = 0;
    while (x != 0) {
        lret = lret * 10 + x % 10;
        x /= 10;
    }
    if ((int) lret != lret) {
        return isOverLength;
    }
    return (int) lret;

}
