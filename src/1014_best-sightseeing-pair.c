//
/* Created by rock on 6/18/20.
*/
#include "leetcode_functions.h"
int maxScoreSightseeingPair(int *A, int ASize) {
    int ans = 0;
    int pre_max = A[0] + 0;
    for (int i = 1; i < ASize; ++i) {
        ans = fmax(ans, pre_max + A[i] - i);
        pre_max = fmax(pre_max, A[i] + i);

    }
    return ans;


}