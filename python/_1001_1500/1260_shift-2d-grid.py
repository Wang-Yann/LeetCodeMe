#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 15:41:47
# @Last Modified : 2020-07-05 15:41:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。 
# 
#  每次「迁移」操作将会引发下述活动： 
# 
#  
#  位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。 
#  位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。 
#  位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。 
#  
# 
#  请你返回 k 次迁移操作后最终得到的 二维网格。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[9,1,2],[3,4,5],[6,7,8]]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# 输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# 输出：[[1,2,3],[4,5,6],[7,8,9]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 50 
#  1 <= grid[i].length <= 50 
#  -1000 <= grid[i][j] <= 1000 
#  0 <= k <= 100 
#  
#  Related Topics 数组 
#  👍 25 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col + k) % num_cols
                wrap_around_count = (col + k) // num_cols
                new_row = (row + wrap_around_count) % num_rows
                new_grid[new_row][new_col] = grid[row][col]
        return new_grid


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % (m * n)
        for _ in range(k):
            previous = grid[-1][-1]
            for row in range(m):
                for col in range(n):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
        return grid


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        grid=[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], k=1
    ), [[9, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]),
    pytest.param(dict(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4),
                 [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]),
    pytest.param(dict(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
])
def test_solutions(kwargs, expected):
    assert Solution().shiftGrid(**kwargs) == expected
    assert Solution1().shiftGrid(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
