//
/* Created by rock on 4/29/20.
*/

#include "leetcode_functions.h"


int common_comp(const void *a, const void *b)//用来做比较的函数。
{
    return *(int *) a - *(int *) b;
}

int cmp(const void *a, const void *b) {
    int *ap = *(int **) a;
    int *bp = *(int **) b;
    if (ap[0] == bp[0])
        return ap[1] - bp[1];
    else
        return ap[0] - bp[0];

}

int findLongestChain(int **pairs, int pairsSize, int *pairsColSize) {
    int *dp = (int *) malloc(sizeof(int) * pairsSize);
    int i, j;
    int max = 0;

    qsort(pairs, pairsSize, sizeof(pairs[0]), cmp);//调用qsort排序

    for (i = 0; i < pairsSize; ++i) {
        dp[i] = 1;
    }

    for (i = 0; i < pairsSize; ++i) {
        for (j = 0; j < i; ++j) {
            if (pairs[i][0] > pairs[j][1]) {
                dp[i] = fmax(dp[i], dp[j] + 1);
            }

        }

    }
    for (i = 0; i < pairsSize; ++i) {
        max = fmax(max, dp[i]);
    }
    return max;


}