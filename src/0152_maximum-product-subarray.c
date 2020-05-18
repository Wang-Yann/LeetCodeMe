//
/* Created by rock on 5/18/20.
*/

#include "leetcode_functions.h"
int maxProduct(int* nums, int numsSize){
    int global_max = INT_MIN;
    int local_max = 1;
    int local_min = 1;
    for (int i = 0; i < numsSize; ++i) {
        local_max = max(1, local_max);
        int x = nums[i];
        int pre_local_max = local_max;
        int pre_local_min = local_min;
        if (x > 0) {
            local_max = pre_local_max * x;
            local_min= pre_local_min * x;
        } else {
            local_max = pre_local_min * x;
            local_min= pre_local_max * x;
        }
        global_max = max(local_max, global_max);

    }
    return global_max;

}