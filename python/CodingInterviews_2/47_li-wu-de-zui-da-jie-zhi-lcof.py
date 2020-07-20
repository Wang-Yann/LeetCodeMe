#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:51:41
# @Last Modified : 2020-05-10 18:51:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#
#
#  示例 1:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
#
#
#  提示：
#
#
#  0 < grid.length <= 200
#  0 < grid[0].length <= 200
#
#  Related Topics 动态规划
#  👍 49 👎 0


from typing import List

import pytest


class Solution:

    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n+1) for _ in range(m +1)]
        for j in range(n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m-1][n-1]


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]
     ], 12),
    ([[1]],1)
])
def test_solutions(args, expected):
    assert Solution().maxValue(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
