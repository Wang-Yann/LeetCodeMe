#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 21:54:19
# @Last Modified : 2020-07-22 21:54:19
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 整数可以被看作是其因子的乘积。 
# 
#  例如： 
# 
#  8 = 2 x 2 x 2;
#   = 2 x 4. 
# 
#  请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。 
# 
#  注意： 
# 
#  
#  你可以假定 n 为永远为正数。 
#  因子必须大于 1 并且小于 n。 
#  
# 
#  示例 1： 
# 
#  输入: 1
# 输出: []
#  
# 
#  示例 2： 
# 
#  输入: 37
# 输出: [] 
# 
#  示例 3： 
# 
#  输入: 12
# 输出:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ] 
# 
#  示例 4: 
# 
#  输入: 32
# 输出:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
#  
#  Related Topics 回溯算法 
#  👍 34 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getFactors(self, n: int) -> List[List[int]]:
        """GOOD"""
        res = []

        def dfs(num, factors):
            i = 2 if not factors else factors[-1]
            while i <= num // i:
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
                    res.append(list(factors))
                    factors.pop()
                    dfs(num // i, factors)
                    factors.pop()
                i += 1

        dfs(n, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, []),
    (37, []),
    (12, [
        [2, 6],
        [2, 2, 3],
        [3, 4]
    ]),
    (32, [
        [2, 16],
        [2, 2, 8],
        [2, 2, 2, 4],
        [2, 2, 2, 2, 2],
        [2, 4, 4],
        [4, 8]
    ]
     ),
])
def test_solutions(args, expected):
    assert sorted(Solution().getFactors(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
