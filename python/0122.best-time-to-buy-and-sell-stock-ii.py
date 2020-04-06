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

"""
贪心算法
&&&&&&&&&&&
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            if delta > 0:
                profit_max += delta
        return profit_max

    def maxProfitPeakValley(self, prices: List[int]) -> int:
        if not prices:
            return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        length = len(prices)
        while i < length - 1:
            while i < length - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < length - 1 and  prices[i]<=prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit

    def maxProfitSmSimple(self, prices: List[int]) -> int:
        """
            dp[i][k][0 or 1]
            0 <= i <= n-1, 1 <= k <= K
            n 为天数，大 K 为最多交易数
            1 表示持有，0 表示没有持有
            此问题共 n × K × 2 种状态，全部穷举
        """
        if not prices:
            return 0
        n = len(prices)
        s_range = (0, 1)
        dp = [[0] * len(s_range) for x in range(0, n)]
        dp[-1][1] = - float('inf')
        for i in range(0, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i-1][0]-prices[i])

        return dp[n - 1][0]


if __name__ == '__main__':
    sol = Solution()
    sample = [7, 1, 5, 3, 6, 4]
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [7, 6, 4, 3, 1]
    print(sol.maxProfit(sample))
    print(sol.maxProfit(sample1))
    print(sol.maxProfit(sample2))

    print(sol.maxProfitPeakValley(sample))
    print(sol.maxProfitPeakValley(sample1))
    print(sol.maxProfitPeakValley(sample2))

    print(sol.maxProfitSmSimple(sample),sol.maxProfitSmSimple(sample1),sol.maxProfitSmSimple(sample2))
