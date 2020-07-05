#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 18:41:36
# @Last Modified : 2020-07-05 18:41:36
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。 
# 
#  如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样
# 的路径，则返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入： 
# grid = 
# [[0,0,0],
# [1,1,0],
#  [0,0,0],
# [0,1,1],
#  [0,0,0]], 
# k = 1
# 输出：6
# 解释：
# 不消除任何障碍的最短路径是 10。
# 消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3
# ,2) -> (4,2).
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：
# grid = 
# [[0,1,1],
# [1,1,1],
# [1,0,0]], 
# k = 1
# 输出：-1
# 解释：
# 我们至少需要消除两个障碍才能找到这样的路径。
#  
# 
#  
# 
#  提示： 
# 
#  
#  grid.length == m 
#  grid[0].length == n 
#  1 <= m, n <= 40 
#  1 <= k <= m*n 
#  grid[i][j] == 0 or 1 
#  grid[0][0] == grid[m-1][n-1] == 0 
#  
#  Related Topics 广度优先搜索 
#  👍 58 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """GOOD"""
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        queue = collections.deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}
        if k > (m - 1 + n - 1):
            return m - 1 + n - 1
        while queue:
            row, col, eliminate, steps = queue.popleft()
            for nr, nc in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
                if 0 <= nr <= m - 1 and 0 <= nc <= n - 1:
                    if grid[nr][nc] == 1 and eliminate > 0 and (nr, nc, eliminate - 1) not in visited:
                        visited.add((nr, nc, eliminate - 1))
                        queue.append((nr, nc, eliminate-1, steps + 1))
                    if grid[nr][nc] == 0 and (nr, nc, eliminate) not in visited:
                        if nr == m - 1 and nc == n - 1:
                            return steps + 1
                        visited.add((nr, nc, eliminate))
                        queue.append((nr, nc, eliminate, steps + 1))
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(grid=[[0, 0, 0],
                [1, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 0]],
          k=1
          ), 6),
    pytest.param(dict(grid=[[0, 1, 1],
                            [1, 1, 1],
                            [1, 0, 0]],
                      k=1
                      ), -1),
])
def test_solutions(kwargs, expected):
    assert Solution().shortestPath(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
