#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。 
# 
#  我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。 
# 
#  如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：d = 1, f = 6, target = 3
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：d = 2, f = 6, target = 7
# 输出：6
#  
# 
#  示例 3： 
# 
#  输入：d = 2, f = 5, target = 10
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：d = 1, f = 2, target = 3
# 输出：0
#  
# 
#  示例 5： 
# 
#  输入：d = 30, f = 30, target = 500
# 输出：222616187 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= d, f <= 30 
#  1 <= target <= 1000 
#  
#  Related Topics 动态规划

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        AC
        纪念下
        """
        CHOICES = list(range(1, f + 1))
        MOD = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(n, t):
            if t <= 0 or n <= 0:
                return 0
            if n == 1:
                return 1 if 1 <= t <= f else 0
            return sum(dp(n - 1, t - choice) % MOD for choice in CHOICES)

        return dp(d, target) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(d=1, f=6, target=3), 1],
    [dict(d=2, f=6, target=7), 6],
    [dict(d=2, f=5, target=10), 1],
    [dict(d=1, f=2, target=3), 0],
    [dict(d=30, f=30, target=500), 222616187],
])
def test_solutions(kw, expected):
    assert Solution().numRollsToTarget(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
