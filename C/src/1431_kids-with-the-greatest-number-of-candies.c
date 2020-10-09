//
/* Created by rock on 6/1/20.
*/
#include "leetcode_functions.h"

bool *kidsWithCandies(int *candies, int candiesSize, int extraCandies, int *returnSize) {
    bool *res = (bool *) malloc(candiesSize * sizeof(bool));
    int max_v = *candies;
    for (int i = 0; i < candiesSize; ++i) {
        if (candies[i] > max_v) {
            max_v = candies[i];
        }
    }
    for (int i = 0; i < candiesSize; ++i) {
        if (candies[i] + extraCandies >= max_v) {
            res[i] = true;
        } else {
            res[i] = false;
        }

    }
    *returnSize = candiesSize;
    return res;

}
