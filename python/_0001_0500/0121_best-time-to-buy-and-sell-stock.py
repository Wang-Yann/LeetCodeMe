#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
#  如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
#  注意：你不能在买入股票前卖出股票。
#
#
#
#  示例 1:
#
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#
#
#  示例 2:
#
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#  Related Topics 数组 动态规划
#  👍 1081 👎 0
from typing import List

import pytest


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


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
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
        N = len(prices)

        k_range = (0, 1)
        s_range = (0, 1)
        dp = [[[0] * len(s_range) for _ in k_range] for __ in range(N)]
        for row in dp:
            for col in row:
                col[1] = float("-inf")
        # print(dp)
        for i in range(N):
            for k in k_range:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], -prices[i])

        return dp[N - 1][1][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
            1 表示持有，0 表示没有持有
        """
        if not prices:
            return 0
        N = len(prices)
        s_range = (0, 1)
        dp = [[0] * len(s_range) for _ in range(N)]
        dp[-1][1] = - float('inf')
        for i in range(N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        # print(dp)

        return dp[N - 1][0]


@pytest.mark.parametrize("args,expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([7, 1, 5, 3, 6, 4], 5),
])
def test_solutions(args, expected):
    assert Solution().maxProfit(args) == expected
    assert Solution1().maxProfit(args) == expected
    assert Solution2().maxProfit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
