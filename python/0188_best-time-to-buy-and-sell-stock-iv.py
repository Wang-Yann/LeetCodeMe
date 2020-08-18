#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  示例 1:
#
#  输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
#
#  示例 2:
#
#  输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3
# 。
#
#  Related Topics 动态规划
#  👍 251 👎 0

"""
import math
from typing import List

import pytest


class Solution:

    def maxProfitInf(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        states = (0, 1)
        dp = [[0] * len(states) for _ in range(N)]
        dp[-1][1] = - math.inf
        for i in range(N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[N - 1][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        TODO
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        """
        if not prices:
            return 0
        MAX_K = k
        N = len(prices)
        if MAX_K > N // 2:
            return self.maxProfitInf(prices)

        k_choices = range(MAX_K + 1)
        states = (0, 1)
        dp = [[[0] * len(states) for _ in k_choices] for _ in range(N)]
        for ki in k_choices:
            dp[0][ki][1] = float("-inf")
            dp[-1][ki][1] = float("-inf")
        for i in range(N):
            # for k in range(max_k, 0, -1):
            for k in range(1, MAX_K + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[N - 1][MAX_K][0]


class Solution1(object):
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2:
            return self.maxAtMostNPairsProfit(prices)
        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in range(k + 1)]
        max_sell = [0 for _ in range(k + 1)]

        for i in range(len(prices)):
            for j in range(1, min(k, i // 2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]


@pytest.mark.parametrize("kw,expected", [
    [dict(prices=[2, 4, 1], k=2), 2],
    [dict(prices=[3, 2, 6, 5, 0, 3], k=2), 7],
])
def test_solutions(kw, expected):
    assert Solution().maxProfit(**kw) == expected
    assert Solution1().maxProfit(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
