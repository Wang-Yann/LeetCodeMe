#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 14:18:15
# @Last Modified : 2020-04-12 14:18:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#  示例:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#  Related Topics 数组 动态规划
#  👍 522 👎 0

"""

from typing import List

import pytest


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """AC"""
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for col in range(n + 1):
            dp[0][col] = 0x7fffffff
        for row in range(m + 1):
            dp[row][0] = 0x7fffffff
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[0][0]
                    continue
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i - 1][j - 1]
        return dp[m][n]


class Solution1:
    def minPathSum(self, grid):
        sum_array = list(grid[0])
        for j in range(1, len(grid[0])):
            sum_array[j] = sum_array[j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            sum_array[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                sum_array[j] = min(sum_array[j - 1], sum_array[j]) + grid[i][j]

        return sum_array[-1]


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(R)]
        dp[0][0] = grid[0][0]
        for i in range(1, R):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, C):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[R - 1][C - 1]


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]
     ], 7)
])
def test_solutions(args, expected):
    assert Solution().minPathSum(args) == expected
    assert Solution1().minPathSum(args) == expected
    assert Solution2().minPathSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
