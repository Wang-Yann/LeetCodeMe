#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划

"""
import functools
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    """DP
    完全背包
    凑零钱问题的暴力解法就是遍历一棵 N 叉树
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        return dp[amount] if dp[amount] != math.inf else -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 0x7fffffff

        @functools.lru_cache(None)
        def dp(n):
            if n == 0:
                return 0
            elif n < 0:
                return -1
            res = INF
            for coin in coins:
                sub_problem = dp(n - coin)
                if sub_problem == -1:
                    continue
                res = min(res, 1 + sub_problem)
            return res if res != INF else -1

        return dp(amount)


@pytest.mark.parametrize("kw,expected", [
    [dict(coins=[1, 2, 5], amount=11), 3],
    [dict(coins=[2], amount=3), -1],
])
def test_solutions(kw, expected):
    assert Solution().coinChange(**kw) == expected
    assert Solution1().coinChange(**kw) == expected
    assert Solution2().coinChange(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
