#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-08 11:22:18
# @Last Modified : 2020-04-08 11:22:18
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#
#
#  示例 1：
#
#  输入：m = 2, n = 3, k = 1
# 输出：3
#
#
#  示例 2：
#
#  输入：m = 3, n = 1, k = 0
# 输出：1
#
#
#  提示：
#
#
#  1 <= n,m <= 100
#  0 <= k <= 20
#
#  👍 124 👎 0

from typing import List

import pytest


class Solution:
    bit_array = []

    def movingCount(self, m: int, n: int, k: int) -> int:
        area_matrix = [[0 for _ in range(n)] for _ in range(m)]
        self.bit_array = [self.getNumBitSum(x) for x in range(max(m, n))]
        res = self.dfs(area_matrix, m - 1, n - 1, 0, 0, k)
        return res

    def getNumBitSum(self, num: int) -> int:
        v = 0
        while num > 0:
            v += num % 10
            num //= 10
        return v

    def dfs(self, area_array: List[List[int]], rows: int, cols: int, i: int, j: int, k: int):
        if i < 0 or i > rows or j < 0 or j > cols or area_array[i][j] or self.bit_array[i] + self.bit_array[j] > k:
            return 0
        area_array[i][j] = 1
        return 1 + self.dfs(area_array, rows, cols, i, j - 1, k) \
               + self.dfs(area_array, rows, cols, i, j + 1, k) \
               + self.dfs(area_array, rows, cols, i - 1, j, k) \
               + self.dfs(area_array, rows, cols, i + 1, j, k)


@pytest.mark.parametrize("args,expected", [
    ([11, 11, 5], 21),
    ([2, 3, 1], 3),
    ([3, 1, 0], 1),
])
def test_solutions(args, expected):
    assert Solution().movingCount(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
