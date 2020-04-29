#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 16:41:34
# @Last Modified : 2020-04-29 16:41:34
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
