#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 00:02:47
# @Last Modified : 2020-07-12 00:02:47
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#  
# 
#  示例 2： 
# 
#  输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#  
#  Related Topics 数组 
#  👍 10 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = set()
        cols = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ]),
    pytest.param(
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ],
        [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]),
])
def test_solutions(args, expected):
    Solution().setZeroes(args)
    assert args == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
