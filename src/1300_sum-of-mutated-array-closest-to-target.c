//
/* Created by rock on 6/14/20.
*/

#include "leetcode_functions.h"

int cmp(const void *c1, const void *c2) {
    return *(int *) c1 - *(int *) c2;

}
//先按递增排序；
//然后一趟遍历，发现当下值大于（目标值减去累加和除以剩下个数的值）时，则返回剩余的平均值
int findBestValue(int *arr, int arrSize, int target) {
    if (arr == NULL) {
        return 0;
    }
    qsort(arr, arrSize, sizeof(int), cmp);
    int sum = 0;
    for (int i = 0; i < arrSize; ++i) {
        int x = (target - sum) / (arrSize - i);
        if (x < arr[i]) {
            double t = ((double) (target - sum) / (arrSize - i));
            if (t - x > 0.5) {
                return x + 1;
            } else {
                return x;
            }
        }
        sum += arr[i];

    }
    return arr[arrSize - 1];


};