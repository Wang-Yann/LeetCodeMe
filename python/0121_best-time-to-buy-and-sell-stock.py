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
import numpy as np


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit_list = [0]
        max_sofar, max_result = 0, 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            max_sofar = max(max_sofar + delta, delta)
            max_result = max(max_result, max_sofar)
            profit_list.append(max_result)
            # temp_list.append(max_sofar)
        # print(profit_list, temp_list)
        return max(profit_list)

    def maxProfitSm(self, prices: List[int]) -> int:
        """
            dp[i][k][0 or 1]
            0 <= i <= n-1, 1 <= k <= K
            n 为天数，大 K 为最多交易数
            1 表示持有，0 表示没有持有
            此问题共 n × K × 2 种状态，全部穷举
        """
        # dp_array = np.zeros((n,2,2),np.int)
        # print(dp_array)
        if not prices:
            return 0
        n = len(prices)

        k_range = (0, 1)
        s_range = (0, 1)
        dp = [[[0] * len(s_range)] * len(k_range) for x in range(0, n)]
        for row in dp:
            for col in row:
                col[1] = float("-inf")
            row[0][1] = float("-inf")
        for i in range(0, n):
            for k in k_range:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], -prices[i])

        return dp[n - 1][1][0]

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
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        # print(dp)

        return dp[n - 1][0]


if __name__ == '__main__':
    sol = Solution()
    sample = [7, 1, 5, 3, 6, 4]
    sample1 = [7, 6, 4, 3, 1]
    sample2 = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(sample), sol.maxProfit(sample1), sol.maxProfit(sample2))
    print(sol.maxProfitSm(sample),sol.maxProfitSm(sample1),sol.maxProfitSm(sample2))
    print(sol.maxProfitSmSimple(sample),sol.maxProfitSmSimple(sample1),sol.maxProfitSmSimple(sample2))
