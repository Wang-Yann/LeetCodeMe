#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 15:02:01
# @Last Modified : 2020-07-05 15:02:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。 
# 
#  另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。 
# 
#  你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。 
# 
#  请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 2, m = 3, indices = [[0,1],[1,1]]
# 输出：6
# 解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
# 第一次增量操作后得到 [[1,2,1],[0,1,0]]。
# 最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 2, m = 2, indices = [[1,1],[0,0]]
# 输出：0
# 解释：最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  1 <= m <= 50 
#  1 <= indices.length <= 100 
#  0 <= indices[i][0] < n 
#  0 <= indices[i][1] < m 
#  
#  Related Topics 数组 
#  👍 31 👎 0

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE,BIG_RES







# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        grid =[[0]*m for _ in range(n)]
        for r,c in indices:
            for j  in range(m):
                grid[r][j]+=1
            for i in range(n):
                grid[i][c]+=1
        # print(grid)
        return sum(x%2 for row in grid for x in row )

        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        n = 2, m = 3, indices = [[0,1],[1,1]]
    ), 6),
    pytest.param(dict( n = 2, m = 2, indices = [[1,1],[0,0]]  ), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().oddCells(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

