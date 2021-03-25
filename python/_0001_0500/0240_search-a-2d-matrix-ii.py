#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 16:41:34
# @Last Modified : 2020-04-29 16:41:34
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
#
#  每行的元素从左到右升序排列。
#  每列的元素从上到下升序排列。
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
#  Related Topics 二分查找 分治算法
#  👍 371 👎 0

"""

from typing import List

import pytest


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j =  0, n - 1
        while i <= m - 1 and j >=0:
            if matrix[i][j] < target:
                i+=1
            elif matrix[i][j] > target:
                j-=1
            else:
                return True
        return False


@pytest.mark.parametrize("matrix", [[
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]])
@pytest.mark.parametrize("target,expected", [
    (5, True),
    (20, False),
    (33, False),
])
def test_solutions(matrix, target, expected):
    sol = Solution()
    assert sol.searchMatrix(matrix, target) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
