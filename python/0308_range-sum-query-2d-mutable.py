#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 11:37:29
# @Last Modified : 2020-07-23 11:37:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 2D 矩阵 matrix，请计算出从左上角 (row1, col1) 到右下角 (row2, col2) 组成的矩形中所有元素的和。 
# 
#  
# 上述粉色矩形框内的，该矩形由左上角 (row1, col1) = (2, 1) 和右下角 (row2, col2) = (4, 3) 确定。其中，所包括的元
# 素总和 sum = 8。 
# 
#  示例： 
# 
#  给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#  
# 
#  
# 
#  注意: 
# 
#  
#  矩阵 matrix 的值只能通过 update 函数来进行修改 
#  你可以默认 update 函数和 sumRegion 函数的调用次数是均匀分布的 
#  你可以默认 row1 ≤ row2，col1 ≤ col2 
#  
# 
#  
#  Related Topics 树状数组 线段树 
#  👍 18 👎 0

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:
    """
    链接：https://leetcode-cn.com/problems/range-sum-query-2d-mutable/solution/python-zi-dian-by-frankchen250-2/
    """

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        sum_arr = [[0] * (col + 1) for _ in range(row + 1)]
        self.update_dic = collections.defaultdict(int)

        for i in range(row):
            for j in range(col):
                sum_arr[i + 1][j + 1] = sum_arr[i][j + 1] + sum_arr[i + 1][j] - sum_arr[i][j] + matrix[i][j]
        self.sum_arr = sum_arr
        self.matrix = matrix

    # 更新时间复杂度 O(1)
    def update(self, row: int, col: int, val: int) -> None:
        self.update_dic[(row, col)] = val - self.matrix[row][col]

    # 求和时间复杂度 O(N)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p1 = self.sum_arr[row2 + 1][col2 + 1]
        p2 = self.sum_arr[row2 + 1][col1]
        p3 = self.sum_arr[row1][col2 + 1]
        p4 = self.sum_arr[row1][col1]
        s = p1 - p2 - p3 + p4
        for (row, col), val in self.update_dic.items():
            if row1 <= row <= row2 and col1 <= col <= col2:
                s += val
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    s = NumMatrix(matrix)

    assert s.sumRegion(2, 1, 4, 3) == 8
    s.update(3, 2, 2)
    assert s.sumRegion(2, 1, 4, 3) == 10


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
