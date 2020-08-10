#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#
#  示例 1:
#
#  输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#
#
#  示例 2:
#
#  输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
#
#  示例 3:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
#  提示：
#
#
#  1 <= prices.length <= 3 * 10 ^ 4
#  0 <= prices[i] <= 10 ^ 4
#
#  Related Topics 贪心算法 数组
#  👍 782 👎 0
from typing import List

import pytest


class Solution:
    """
    贪心算法
    &&&&&&&&&&&
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            if delta > 0:
                profit_max += delta
        return profit_max


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """PeakValley"""
        if not prices:
            return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_profit = 0
        length = len(prices)
        while i < length - 1:
            while i < length - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < length - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
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
        dp = [[0] * len(s_range) for _ in range(n)]
        dp[-1][1] = - float('inf')
        for i in range(0, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]


@pytest.mark.parametrize("args,expected", [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution, Solution1, Solution2
])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().maxProfit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
