#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 14:20:57
# @Last Modified : 2020-07-15 14:20:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。 
# 
#  返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 
# 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。 
# 
#  示例 1: 
# 
#  输入:
# [
#   [1,0,1],
#   [0,0,1],
#   [0,0,1]
# ]
# 输出: [1,0,2]
# 解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
#  
# 
#  示例 2: 
# 
#  输入:
# [
#   [0,1,1],
#   [1,0,1],
#   [1,1,0]
# ]
# 输出: [0,0,1]
#  
# 
#  提示： 
# 
#  
#  matrix.length == matrix[0].length <= 200 
#  
#  Related Topics 动态规划 
#  👍 12 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        """
        1139 TODO
        https://leetcode.com/problems/largest-1-bordered-square/discuss/345233/JavaC%2B%2BPython-Straight-Forward
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] ^= 1
        top, left = [a[:] for a in matrix], [a[:] for a in matrix]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i:
                        top[i][j] = top[i - 1][j] + 1
                    if j:
                        left[i][j] = left[i][j - 1] + 1
        for r in range(min(m, n), 0, -1):
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1],
                           left[i][j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return [i, j, r]
        return []


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [
                [1, 0, 1],
                [0, 0, 1],
                [0, 0, 1]
            ], [1, 0, 2]
    ),
    (
            [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]
            ], [0, 0, 1]
    )
])
def test_solutions(args, expected):
    assert Solution().findSquare(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
