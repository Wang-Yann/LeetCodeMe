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
