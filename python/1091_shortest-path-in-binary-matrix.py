#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。 
# 
#  一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成： 
# 
#  
#  相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角） 
#  C_1 位于 (0, 0)（即，值为 grid[0][0]） 
#  C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]） 
#  如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0） 
#  
# 
#  返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,0]]
# 
# 输出：2
# 
#  
# 
#  示例 2： 
# 
#  输入：[[0,0,0],[1,1,0],[1,1,0]]
# 
# 输出：4
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 广度优先搜索

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = collections.deque([(0, 0)])
        dest = (m - 1, n - 1)
        res = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while dq:
            res += 1
            dq_len = len(dq)
            for _ in range(dq_len):
                i, j = dq.popleft()
                if 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == 0:
                    grid[i][j] = 1
                    if (i, j) == dest:
                        return res
                    for x, y in directions:
                        dq.append((i + x, j + y))
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 1],
      [1, 0]], 2),
    ([[0, 0, 0],
      [1, 1, 0],
      [1, 1, 0]], 4),
])
def test_solutions(args, expected):
    assert Solution().shortestPathBinaryMatrix(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
