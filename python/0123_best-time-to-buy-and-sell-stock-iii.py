#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#  示例 1:
#
#  输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
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
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#  Related Topics 数组 动态规划
#  👍 447 👎 0
from typing import List

import pytest


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        贪心算法
        &&&&&&&&&&&

        
            dp[i][k][0 or 1]
            0 <= i <= n-1, 1 <= k <= K
            n 为天数，大 K 为最多交易数
            1 表示持有，0 表示没有持有
            此问题共 n × K × 2 种状态，全部穷举
        """
        if not prices:
            return 0
        N = len(prices)
        max_k = 2
        k_range = (0, 1, 2)
        s_range = (0, 1)
        dp = [[[0] * len(s_range) for _ in k_range] for __ in range(N)]
        for ki in k_range:
            dp[0][ki][1] = float("-inf")
            dp[-1][ki][1] = float("-inf")
        for i in range(N):
            # for k in range(max_k, 0, -1):
            for k in range(1, max_k + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

        return dp[N - 1][max_k][0]


@pytest.mark.parametrize("args,expected", [
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().maxProfit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
