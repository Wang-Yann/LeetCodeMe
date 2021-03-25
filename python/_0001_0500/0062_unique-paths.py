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
#  问总共有多少条不同的路径？
#
#
#
#  例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
#
#
#  示例 1:
#
#  输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
#
#
#  示例 2:
#
#  输入: m = 7, n = 3
# 输出: 28
#
#
#
#  提示：
#
#
#  1 <= m, n <= 100
#  题目数据保证答案小于等于 2 * 10 ^ 9
#
#  Related Topics 数组 动态规划
#  👍 609 👎 0

"""
import pytest


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        (1,1)-->(m,n)
        F(m,n) = F(m-1,n)+F(m,n-1)
        """
        # if m==1 or n ==1: return 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:
                    continue
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m][n]


class Solution1:
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]

        return ways[n - 1]


@pytest.mark.parametrize("args,expected", [
    ([3, 2], 3),
    ([7, 3], 28),
    ([33, 11], 1471442973),
    ([1, 1], 1),
    ([1, 10], 1),
    ([10, 1], 1),
])
def test_solutions(args, expected):
    assert Solution().uniquePaths(*args) == expected
    assert Solution1().uniquePaths(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
