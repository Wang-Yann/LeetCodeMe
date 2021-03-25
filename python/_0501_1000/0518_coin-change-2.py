#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
#  
# 
#  
#  
# 
#  示例 1: 
# 
#  输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  示例 2: 
# 
#  输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#  
# 
#  示例 3: 
# 
#  输入: amount = 10, coins = [10] 
# 输出: 1
#  
# 
#  
# 
#  注意: 
# 
#  你可以假设： 
# 
#  
#  0 <= amount (总金额) <= 5000 
#  1 <= coin (硬币面额) <= 5000 
#  硬币种类不超过 500 种 
#  结果符合 32 位符号整数 
#  
# 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        amount=5, coins=[1, 2, 5]
    ), 4),
    pytest.param(dict(amount=3, coins=[2]), 0),
    pytest.param(dict(amount=10, coins=[10]), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().change(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
