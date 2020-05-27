//
/* Created by rock on 5/15/20.
*/
#include "leetcode_functions.h"
#define INIT_LEN 100000
int subarraysDivByK(int* A, int ASize, int K){
    int lookup[INIT_LEN]={ 0 };
    int res = 0;
    int prefix = 0;
    lookup[0] = 1;
    for (int i = 0; i < ASize; ++i) {
        prefix = (prefix + *(A+i)) % K;
        while (prefix < 0) {
            prefix += K;
        }
        res+=lookup[prefix];
        lookup[prefix]++;
    }
    return res;

}