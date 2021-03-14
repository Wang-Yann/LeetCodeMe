#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 17:56:21
# @Last Modified : 2020-04-11 17:56:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
#  示例 1:
#
#  输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
#  示例 2:
#
#  输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#  Related Topics 数组
#  👍 424 👎 0

"""

from typing import List

import pytest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        R, C = len(matrix), len(matrix[0])
        cnt = 0
        min_i, min_j = 0, 0
        max_i, max_j = R - 1, C - 1
        direction = 0
        while cnt < R * C:
            # --->
            if direction == 0:
                for idx in range(min_j, max_j + 1):
                    res.append(matrix[min_i][idx])
                    cnt += 1
                min_i += 1
            # |
            # V
            elif direction == 1:
                for idx in range(min_i, max_i + 1):
                    res.append(matrix[idx][max_j])
                    cnt += 1
                max_j -= 1
            # <--
            elif direction == 2:
                for idx in range(max_j, min_j - 1, -1):
                    res.append(matrix[max_i][idx])
                    cnt += 1
                max_i -= 1
            # ^
            # |
            elif direction == 3:
                for idx in range(max_i, min_i - 1, -1):
                    res.append(matrix[idx][min_j])
                    cnt += 1
                min_j += 1
            direction = (direction + 1) % 4
        return res


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        R, C = len(matrix), len(matrix[0])
        visited = [[False] * C for _ in range(R)]
        total = R * C
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        direction = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            next_row, next_column = row + directions[direction][0], column + directions[direction][1]
            if not (0 <= next_row <= R - 1 and 0 <= next_column <= C - 1 and not visited[next_row][next_column]):
                direction = (direction + 1) % 4
            row += directions[direction][0]
            column += directions[direction][1]
        return order


@pytest.mark.parametrize("args,expected", [
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],
     [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12], ],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1]], [1]),
    ([[1, 2],
      [3, 4]],
     [1, 2, 4, 3]),
    ([[1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25], ],
     [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().spiralOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
