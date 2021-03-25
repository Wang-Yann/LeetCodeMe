#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 14:54:42
# @Last Modified : 2020-04-12 14:54:42
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
#  示例 1:
#
#  输入:
# [
#  [1,1,1],
#  [1,0,1],
#  [1,1,1]
# ]
# 输出:
# [
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
# ]
#
#
#  示例 2:
#
#  输入:
# [
#  [0,1,2,0],
#  [3,4,5,2],
#  [1,3,1,5]
# ]
# 输出:
# [
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
# ]
#
#  进阶:
#
#
#  一个直接的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
#  你能想出一个常数空间的解决方案吗？
#
#  Related Topics 数组
#  👍 252 👎 0

"""
import copy
from typing import List

import pytest


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        clean_rows = set()
        clean_cols = set()
        i = 0
        while i <= m - 1:
            for j in range(n):
                if matrix[i][j] == 0:
                    clean_rows.add(i)
                    clean_cols.add(j)
            i += 1
        for i in clean_rows:
            for col in range(n):
                matrix[i][col] = 0
        for j in clean_cols:
            for row in range(m):
                matrix[row][j] = 0


class Solution1:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]
     ],
     [
         [1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]
     ]),
    ([
         [0, 1, 2, 0],
         [3, 4, 5, 2],
         [1, 3, 1, 5]
     ],
     [
         [0, 0, 0, 0],
         [0, 4, 5, 0],
         [0, 3, 1, 0]
     ])
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    mt = copy.deepcopy(args)
    SolutionCLS().setZeroes(mt)
    assert mt == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
