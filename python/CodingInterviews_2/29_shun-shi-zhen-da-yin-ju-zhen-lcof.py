#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 23:03:57
# @Last Modified : 2020-05-06 23:03:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#
#
#  示例 1：
#
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
#  示例 2：
#
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
#  限制：
#
#
#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
#
#
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#  Related Topics 数组
#  👍 109 👎 0
from typing import List

import pytest


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Good"""
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        l, r, t, b, res = 0, cols - 1, 0, rows - 1, []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left to right
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r:
                break
        return res


@pytest.mark.parametrize("args,expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    pytest.param([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                 [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
])
def test_solutions(args, expected):
    assert Solution().spiralOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
