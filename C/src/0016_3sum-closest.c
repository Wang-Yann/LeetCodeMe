//
/* Created by rock on 6/25/20.
*/

#include "leetcode_functions.h"

int cmp(const void * a, const void * b){
    return *(int *) a - *(int *) b;
}

int threeSumClosest(int* nums, int numsSize, int target){
    int n = numsSize;
    qsort(nums, n, sizeof(int), cmp);
    int best = 1e7;

    for (int i = 0; i < n; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        int j = i + 1;
        int k = n - 1;
        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            if (sum == target) {
                return sum;
            }
            if (abs(sum - target) < abs(best - target)) {
                best = sum;
            }
            if (sum > target) {
                // 如果和大于 target，移动 c 对应的指针
                int k0 = k - 1;
                while (j < k0 && nums[k0] == nums[k]) {
                    --k0;
                }
                k = k0;
            } else {
                // 如果和小于 target，移动 b 对应的指针
                int j0 = j + 1;
                // 移动到下一个不相等的元素
                while (j0 < k && nums[j0] == nums[j]) {
                    ++j0;
                }
                j = j0;
            }

        }


    }
    return best;


}