#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:54:05
# @Last Modified : 2020-07-06 23:54:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m * n 的整数矩阵 mat ，请你将同一条对角线上的元素（从左上到右下）按升序排序后，返回排好序的矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# 输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 排序 数组 
#  👍 15 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(ROWS):
            for j in range(COLS):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(ROWS):
            for j in range(COLS):
                mat[i][j] = d[i - j].pop()
        return mat


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        mat=[[3, 3, 1, 1],
             [2, 2, 1, 2],
             [1, 1, 1, 2]]
    ), [[1, 1, 1, 1],
        [1, 2, 2, 2],
        [1, 2, 3, 3]]),
])
def test_solutions(kwargs, expected):
    assert Solution().diagonalSort(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
