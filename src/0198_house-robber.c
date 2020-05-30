//
/* Created by rock on 5/14/20.
*/
#include "leetcode_functions.h"
int rob(int* nums, int numsSize){
    int *dp = (int *) malloc(sizeof(int) * numsSize);
    int i;
    if (numsSize <= 0) {
        return 0;
    }
    dp[0] = nums[0];
    if (numsSize > 1) {
        dp[1] = fmax(nums[0], nums[1]);
    }
    for (i = 2; i < numsSize; ++i) {
        dp[i] = fmax(dp[i - 2] + nums[i], dp[i - 1]);
    }
    return dp[numsSize - 1];



}