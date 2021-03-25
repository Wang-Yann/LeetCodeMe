#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 15:26:52
# @Last Modified : 2020-08-07 15:26:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# （这是一个交互题） 
# 
#  我们称只包含元素 0 或 1 的矩阵为二进制矩阵。矩阵中每个单独的行都按非递减顺序排序。 
# 
#  给定一个这样的二进制矩阵，返回至少包含一个 1 的最左端列的索引（从 0 开始）。如果这样的列不存在，返回 -1。 
# 
#  您不能直接访问该二进制矩阵。你只可以通过 BinaryMatrix 接口来访问。 
# 
#  
#  BinaryMatrix.get(row, col) 返回位于索引 (row, col) （从 0 开始）的元素。 
#  BinaryMatrix.dimensions() 返回含有 2 个元素的列表 [rows, cols]，表示这是一个 rows * cols的矩阵。 
#  
# 
#  如果提交的答案调用 BinaryMatrix.get 超过 1000 次，则该答案会被判定为错误答案。提交任何试图规避判定机制的答案将会被取消资格。 
# 
#  下列示例中， mat 为给定的二进制矩阵。您不能直接访问该矩阵。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: mat = [[0,0],[1,1]]
# 输出: 0
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: mat = [[0,0],[0,1]]
# 输出: 1
#  
# 
#  示例 3: 
# 
#  
# 
#  
# 输入: mat = [[0,0],[0,0]]
# 输出: -1 
# 
#  示例 4: 
# 
#  
# 
#  
# 输入: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# 输出: 1
#  
# 
#  
# 
#  提示: 
# 
#  
#  rows == mat.length 
#  cols == mat[i].length 
#  1 <= rows, cols <= 100 
#  mat[i][j] 只会是 0 或 1。 
#  mat[i] 已按非递减顺序排序。 
#  
#  Related Topics 数组 
#  👍 4 👎 0

"""

import pytest

mat = []
cnt = 0


class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        global cnt, mat
        cnt += 1
        if 0 <= row <= len(mat) and 0 <= col < len(mat[0]):
            return mat[row][col]

    def dimensions(self):
        return [len(mat), len(mat[0])]


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        R, C = binaryMatrix.dimensions()
        i = 0
        j = C - 1
        while i < R and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        if j == C - 1:
            return -1
        return j + 1

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(mat=[[0, 0], [1, 1]]), 0],
    [dict(mat=[[0, 0], [0, 1]]), 1],
    [dict(mat=[[0, 0], [0, 0]]), -1],
    [dict(mat=[[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]), 1],
])
def test_solutions(kw, expected):
    global cnt, mat
    mat = kw["mat"]
    b = BinaryMatrix()
    res = Solution().leftMostColumnWithOne(b)
    assert res == expected
    assert cnt <= 1000


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
