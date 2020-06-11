//
/* Created by rock on 6/11/20.
*/
#include "leetcode_functions.h"

int *dailyTemperatures(int *T, int TSize, int *returnSize) {
    *returnSize = TSize;
    int *res = malloc(sizeof(int) * TSize);
    //栈底不放元素，因此要多一个空间
    int stack[TSize + 1];
    int stackTop = -1;
    memset(res, 0, sizeof(int) * TSize);
    for (int i = 0; i < TSize; ++i) {
        while (stackTop != -1 && T[stack[stackTop]] < T[i]) {
            int r = stack[stackTop];
            stackTop--;
            res[r] = i - r;
        }
        stack[++stackTop] = i;
    }
    return res;

}