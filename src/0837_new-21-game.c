//
/* Created by rock on 6/6/20.
*/
#include "leetcode_functions.h"

double new21Game(int N, int K, int W) {


    if (K == 0) {
        return 1.0;
    }
    double *dp = (double *) malloc(sizeof(double) * (K + W));
    for (int i = K; i <= N && i < K + W; i++) {
        dp[i] = 1.0;
    }
    dp[K - 1] = 1.0 * fmin(N - K + 1, W) / W;
    for (int i = K - 2; i >= 0; i--) {
        dp[i] = dp[i + 1] - (double)(dp[i + W + 1] - dp[i + 1]) / W;
    }
    return dp[0];


}