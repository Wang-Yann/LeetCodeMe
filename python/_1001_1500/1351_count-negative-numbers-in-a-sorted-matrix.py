#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
# 
#  请你统计并返回 grid 中 负数 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[3,2],[1,0]]
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,-1],[-1,-1]]
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：grid = [[-1]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 100 
#  -100 <= grid[i][j] <= 100 
#  
#  Related Topics 数组 二分查找

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        cnt = 0
        while i >= 0 and j <= n - 1:
            if grid[i][j] < 0:
                cnt += n - j
                i -= 1
            else:
                j += 1
        return cnt


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result, c = 0, n - 1
        for row in grid:
            while c >= 0 and row[c] < 0:
                c -= 1
            result += n - 1 - c
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]), 8],
    [dict(grid=[[3, 2], [1, 0]]), 0],
    [dict(grid=[[1, -1], [-1, -1]]), 3],
    [dict(grid=[[-1]]), 1],
])
def test_solutions(kw, expected):
    assert Solution().countNegatives(**kw) == expected
    assert Solution1().countNegatives(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
