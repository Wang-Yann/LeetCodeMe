#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math
import os
import sys
import traceback
from typing import List


class Solution:

    def maxProfitInf(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        s_range = (0, 1)
        dp = [[0] * len(s_range) for x in range(0, n)]
        dp[-1][1] = - float('inf')
        for i in range(0, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        max_k = k
        n = len(prices)
        if max_k > n // 2:
            return self.maxProfitInf(prices)

        k_range = range(max_k + 1)
        s_range = (0, 1)
        dp = [[[0] * len(s_range) for y in k_range] for x in range(0, n)]
        for ki in k_range:
            dp[0][ki][1] = float("-inf")
            dp[-1][ki][1] = float("-inf")
        for i in range(0, n):
            for k in range(max_k, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[n - 1][max_k][0]


if __name__ == '__main__':
    sol = Solution()
    sample = [2, 4, 1]
    sample1 = [3, 2, 6, 5, 0, 3]
    print(sol.maxProfit(2, sample))
    print(sol.maxProfit(2, sample1))
