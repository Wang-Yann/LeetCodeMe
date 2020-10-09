//
/* Created by rock on 4/28/20.
*/
#include "leetcode_functions.h"



int nthUglyNumber(int n){
    int dp[n];
    dp[0] = 1;
    for (int i = 1; i < n; ++i){
        dp[i]=0;
    }
    int p2 = 0,p3 =0,p5=0;
    int vp2=0,vp3=0,vp5=0;
    int min_val =0;
    for (int i = 1; i < n; ++i) {
        vp2 = dp[p2]*2;
        vp3 =dp[p3]*3;
        vp5 = dp[p5]*5;
        min_val = min(min(vp2,vp5), vp3);
        dp[i] = min_val;
        printf("num:%d--%d\n", dp[i],min_val);
        if (dp[i] == vp2)
            p2++;
        if (dp[i]==vp3)
            p3++;
        if (dp[i] == vp5)
            p5++;
    }
    return dp[n - 1];


}

