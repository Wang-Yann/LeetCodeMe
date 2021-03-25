#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-14 22:04:05
# @Last Modified : 2020-04-14 22:04:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-"1"."0"


"""
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#  示例:
#
#  输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#  Related Topics 动态规划
#  👍 486 👎 0

"""


from typing import List

import pytest


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp(i,j) 表示的是由 1 组成的最大正方形的边长；
        从 (0,0) 开始，对原始矩阵中的每一个 1，我们将当前元素的值更新为
        dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1

        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_side = 0
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


@pytest.mark.parametrize("args,expected",[
   ([
       ["1", "0", "1", "0", "0"],
       ["1", "0", "1", "0", "0"],
       ["1", "1", "1", "0", "0"],
       ["1", "1", "1", "0", "0"],
       ["1", "0", "1", "0", "0"]
   ],4)
])
def test_solutions(args,expected):
    assert Solution().maximalSquare(args)==expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

