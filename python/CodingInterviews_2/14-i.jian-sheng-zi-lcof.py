#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 23:59:54
# @Last Modified : 2020-04-24 23:59:54
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n in (2, 3):
            return n - 1
        dp = [0, 1, 2, 3] + [0] * (n - 4 + 1)
        for i in range(4, n + 1):
            max_val = 0
            for j in range(1, i // 2 + 1):
                max_val = max(dp[j] * dp[i - j], max_val)
            dp[i] = max_val
        # print(dp)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 4, 10
    ]
    res = [sol.cuttingRope(args) for args in samples]
    print(res)
