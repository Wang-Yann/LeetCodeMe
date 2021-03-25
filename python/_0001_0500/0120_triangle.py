#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 20:46:14
# @Last Modified : 2020-04-15 20:46:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
#  相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
#
#
#  例如，给定三角形：
#
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
#
#  说明：
#
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#  Related Topics 数组 动态规划
#  👍 471 👎 0

"""
from typing import List

import pytest


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp[i][j] 表示从三角形顶部走到位置  (i,j) 的最小路径和
        """
        N = len(triangle)
        if not N:
            return 0
        dp = [[0x7fffffff] * N for _ in range(N)]
        dp[0][0] = triangle[0][0]
        for i in range(1, N):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[-1])

    def minimumTotalS(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        cur = triangle[0] + [0x7fffffff]
        for i in range(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in range(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [0x7fffffff]
        return min(cur)


@pytest.mark.parametrize("args,expected", [
    ([
         [2],
         [3, 4],
         [6, 5, 7],
         [4, 1, 8, 3]
     ], 11)
    ,
    ([[-1], [-2, -3]], -4)
])
def test_solutions(args, expected):
    assert Solution().minimumTotal(args) == expected
    assert Solution().minimumTotalS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
