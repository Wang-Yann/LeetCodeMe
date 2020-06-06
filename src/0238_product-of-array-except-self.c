//
/* Created by rock on 6/6/20.
*/
#include "leetcode_functions.h"

int *productExceptSelf(int *nums, int numsSize, int *returnSize) {
    if (numsSize == 0) {
        return NULL;
    }
    int * left_product = (int *) malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        left_product[i] = 1;
    }
    for (int i = 1; i < numsSize; i++) {
        left_product[i] = left_product[i - 1] * nums[i - 1];
    }
    int right_product = 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        right_product *= nums[i+1];
        left_product[i] = left_product[i] * right_product;
    }
    *returnSize = numsSize;
    return left_product;

}
