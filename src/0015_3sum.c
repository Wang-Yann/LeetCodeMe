//
/* Created by rock on 5/13/20.
*/

#include "leetcode_functions.h"


int cmp(const void *a, const void *b) {
    return *(int *) a - *(int *) b;
}

//https://leetcode-cn.com/problems/3sum/solution/cyu-yan-shi-xian-qian-hou-jia-ji-by-dodo-12/
int ** threeSum(int *nums, int numsSize, int *returnSize, int **returnColumnSizes) {
    *returnSize = 0;
    if (numsSize < 3) {
        return NULL;
    }
    //6实验出来的
    int **ret = (int **) malloc(sizeof(int *) * (numsSize + 1) * 6);
    int left = 0;
    int right = numsSize - 1;
    int target = 0;
    *returnColumnSizes = malloc(sizeof(int) * (numsSize + 1) * 6);
    qsort(nums, numsSize, sizeof(int), cmp);
    ret[*returnSize] = malloc(sizeof(int) * 3);

    while (left + 1 < right) {
        int i = left + 1;
        int j = right;
        target = -nums[left];
        while (i < j) {
            if (nums[i] + nums[j] < target) {
                i++;
            } else if (nums[i] + nums[j] > target) {
                j--;
            } else {
                ret[*returnSize][0] = nums[left];
                ret[*returnSize][1] = nums[i];
                ret[*returnSize][2] = nums[j];
                (*returnColumnSizes)[*returnSize] = 3;
                (*returnSize)++;
                ret[*returnSize] = malloc(sizeof(int) * 3);
                while (nums[i] == nums[++i] && i < j) {}
                while (nums[j] == nums[--j] && i < j) {}

            }

        }
        while (nums[left] == nums[++left] && left < right - 1) {}
    }
    return ret;
}