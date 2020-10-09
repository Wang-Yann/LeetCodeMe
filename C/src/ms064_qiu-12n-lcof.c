//
/* Created by rock on 6/2/20.
*/
#include "leetcode_functions.h"
int sumNums(int n){
    if (n == 1) {
        return 1;
    }
    return n+sumNums(n-1);
}