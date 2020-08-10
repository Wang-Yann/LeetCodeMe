#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:34:46
# @Last Modified : 2020-04-22 23:34:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。
#
#
#
#  示例:
#
#  现有矩阵 matrix 如下：
#
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#
#
#
#  限制：
#
#  0 <= n <= 1000
#
#  0 <= m <= 1000
#
#
#
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
#  Related Topics 数组 双指针
#  👍 108 👎 0


from typing import List

import pytest


class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i <= m - 1 and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


@pytest.mark.parametrize("matrix", [
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ],
])
@pytest.mark.parametrize("target,expected", [
    [5, True],
    [20, False]
])
def test_solutions(matrix, target, expected):
    assert Solution().findNumberIn2DArray(matrix, target) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
