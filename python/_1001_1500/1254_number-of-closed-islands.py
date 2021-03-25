#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 15:19:44
# @Last Modified : 2020-07-05 15:19:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。 
# 
#  我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。 
# 
#  如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。 
# 
#  请返回封闭岛屿的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1
# ,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。 
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,1,1,1,1,1],
#             [1,0,0,0,0,0,1],
#             [1,0,1,1,1,0,1],
#             [1,0,1,0,1,0,1],
#             [1,0,1,1,1,0,1],
#             [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[0].length <= 100 
#  0 <= grid[i][j] <=1 
#  
#  Related Topics 深度优先搜索 
#  👍 34 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j, val):
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == 0:
                grid[i][j] = val
                dfs(i, j + 1, val)
                dfs(i + 1, j, val)
                dfs(i - 1, j, val)
                dfs(i, j - 1, val)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j, 1)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0]]), 2),
    (dict(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]), 1),
    pytest.param(dict(grid=[[1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1]]), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().closedIsland(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
