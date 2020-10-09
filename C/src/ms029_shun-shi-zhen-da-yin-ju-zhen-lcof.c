//
/* Created by rock on 6/2/20.
*/
#include "leetcode_functions.h"
//GOOD
int *spiralOrder(int **matrix, int matrixSize, int *matrixColSize, int *returnSize) {
    if (matrix == NULL || matrixSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    *returnSize = matrixSize * matrixColSize[0];
    int *nums = (int *)calloc(*returnSize, sizeof(int));

    int cur = 0, l = 0, t = 0, r = matrixColSize[0] - 1, b = matrixSize - 1;
    while (cur < *returnSize) {
        for (int i = l; cur < *returnSize && i <= r; i++) {
            nums[cur++] = matrix[t][i];
        }
        t++;
        for (int i = t; cur < *returnSize && i <= b; i++) {
            nums[cur++] = matrix[i][r];
        }
        r--;

        for (int i = r; cur < *returnSize && i >= l; i--) {
            nums[cur++] = matrix[b][i];
        }
        b--;

        for (int i = b; cur < *returnSize && i >= t; i--) {
            nums[cur++] = matrix[i][l];
        }
        l++;


    }
    return nums;
}