#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:12:28
# @Last Modified : 2020-04-27 22:12:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        p2, p3, p5 = 0, 0, 0
        for i in range(1,n):
            vp2, vp3, vp5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(vp2, vp3, vp5)
            if dp[i] == vp2:
                p2 += 1
            if dp[i] == vp3:
                p3 += 1
            if dp[i] == vp5:
                p5 += 1
        return dp[n - 1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        1, 10, 12
    ]
    res = [sol.nthUglyNumber(args) for args in samples]
    print(res)
