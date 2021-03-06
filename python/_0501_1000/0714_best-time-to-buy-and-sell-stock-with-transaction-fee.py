#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。 
# 
#  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
# 
#  返回获得利润的最大值。 
# 
#  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 
# 
#  示例 1: 
# 
#  输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8. 
# 
#  注意: 
# 
#  
#  0 < prices.length <= 50000. 
#  0 < prices[i] < 50000. 
#  0 <= fee < 50000. 
#  
#  Related Topics 贪心算法 数组 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        我们维护两个变量  cash 和  hold，前者表示当我们不持有股票时的最大利润，后者表示当我们持有股票时的最大利润。
        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
            # print("price-cash-hold", prices[i], cash, hold)
        return cash


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        if not N:
            return 0
        dp = [[0, -0x80000000] for _ in range(N)]
        for i in range(N):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[N - 1][0]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(prices=[1, 3, 2, 8, 4, 9], fee=2), 8),
])
def test_solutions(kwargs, expected):
    assert Solution().maxProfit(**kwargs) == expected
    assert Solution1().maxProfit(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
