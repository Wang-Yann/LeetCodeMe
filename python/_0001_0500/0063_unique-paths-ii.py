#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 22:16:15
# @Last Modified : 2020-04-11 22:16:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
#  网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#  说明：m 和 n 的值均不超过 100。
#
#  示例 1:
#
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#  Related Topics 数组 动态规划

"""

from typing import List

import pytest


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        (1,1)-->(m,n)
        F(m,n) = F(m-1,n)+F(m,n-1)
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if obstacleGrid[row - 1][col - 1] == 1:
                    dp[row][col] = 0
                elif row == 1 and col == 1:
                    continue
                else:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m][n]


@pytest.mark.parametrize("args,expected", [
    ([
         [0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]
     ], 2),
    ([
         [0, 0, 0],
         [1, 1, 0],
         [0, 0, 0]
     ], 1),
    ([
         [1],
     ], 0),

])
def test_solutions(args, expected):
    assert Solution().uniquePathsWithObstacles(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
