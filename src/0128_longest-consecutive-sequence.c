//
/* Created by rock on 6/6/20.
*/
#include "leetcode_functions.h"
int cmp(const void*a, const void*b)
{
    return (long long)*(int*)a - (long long)*(int*)b;
}

int longestConsecutive(int* a, int n)
{
    if (a == NULL || n == 0) {
        return 0;
    }
    qsort(a, n, sizeof(int), cmp);
    int t =a[0], cnt = 1, max = 1;
    for (int i = 1; i < n; i++) {
        if (a[i] == t) {
            continue;
        } else if ((long long)a[i] - t == 1L) {
            t = a[i];
            cnt++;
            if (max < cnt) {
                max = cnt;
            }
        } else {
            t = a[i];
            cnt = 1;
        }
    }
    return max;
}

