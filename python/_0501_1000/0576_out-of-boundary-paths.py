#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，
# 你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入: m = 2, n = 2, N = 2, i = 0, j = 0
# 输出: 6
# 解释:
# 
#  
# 
#  示例 2： 
# 
#  输入: m = 1, n = 3, N = 3, i = 0, j = 1
# 输出: 12
# 解释:
# 
#  
# 
#  
# 
#  说明: 
# 
#  
#  球一旦出界，就不能再被移动回网格内。 
#  网格的长度和高度在 [1,50] 的范围内。 
#  N 在 [0,50] 的范围内。 
#  Related Topics 深度优先搜索 动态规划

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10 ** 9 + 7
        memo = collections.defaultdict(int)

        # 位置i，j 移动次数k
        def dfs(i, j, k):
            if (i, j, k) not in memo:
                if i < 0 or i >= m or j < 0 or j >= n:
                    memo[(i, j, k)] = 1
                elif k > 0:
                    for x, y in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
                        memo[(i, j, k)] += dfs(x, y, k - 1)
            return memo[(i, j, k)]

        return dfs(i, j, N) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(m=2, n=2, N=2, i=0, j=0), 6),
    pytest.param(dict(m=1, n=3, N=3, i=0, j=1), 12),
])
def test_solutions(kwargs, expected):
    assert Solution().findPaths(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
