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
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/

"""


class Solution:

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
        max_k = 2
        k_range = (0, 1, 2)
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
    sample = [3, 3, 5, 0, 0, 3, 1, 4]
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [7, 6, 4, 3, 1]
    print(sol.maxProfit(sample))
    print(sol.maxProfit(sample1))
    print(sol.maxProfit(sample2))
