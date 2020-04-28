#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 21:46:26
# @Last Modified : 2020-04-27 21:46:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def getKthMagicNumber(self, k: int) -> int:
        p3, p5, p7 = 0, 0, 0
        dp = [1] + [0] * (k - 1)
        for i in range(1, k):
            dp3, dp5, dp7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(dp3, dp5, dp7)
            if dp3 == dp[i]:
                p3 += 1
            if dp5 == dp[i]:
                p5 += 1
            if dp7 == dp[i]:
                p7 += 1
        return dp[k - 1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 5, 10
    ]
    res = [sol.getKthMagicNumber(args) for args in samples]
    print(res)
