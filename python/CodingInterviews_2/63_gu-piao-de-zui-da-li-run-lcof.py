#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 10^5 
# 
#  
# 
#  注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-s
# tock/ 
#  Related Topics 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_sofar = 0
        max_res = 0
        # profit_list = [0]
        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]
            max_sofar = max(max_sofar + delta, delta)
            max_res = max(max_res, max_sofar)
        return max_res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


@pytest.mark.parametrize("args,expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    pytest.param([7, 6, 4, 3, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().maxProfit(args) == expected
    assert Solution1().maxProfit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
