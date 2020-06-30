#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。 
# 
#  只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。 
# 
#  连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。 
# 
#  给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# 输出：[[3, 3], [3, 2]]
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
# 输出：[[1, 3, 3], [2, 3, 3]]
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
# 输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 50 
#  1 <= grid[0].length <= 50 
#  1 <= grid[i][j] <= 1000 
#  0 <= r0 < grid.length 
#  0 <= c0 < grid[0].length 
#  1 <= color <= 1000 
#  
# 
#  
#  Related Topics 深度优先搜索

"""
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        bfs, component, border = [[r0, c0]], {(r0, c0)}, set()
        for r0, c0 in bfs:
            for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                r, c = r0 + i, c0 + j
                if 0 <= r < R and 0 <= c < C and grid[r][c] == grid[r0][c0]:
                    if (r, c) not in component:
                        bfs.append([r, c])
                        component.add((r, c))
                else:
                    border.add((r0, c0))
        for x, y in border:
            grid[x][y] = color
        return grid


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        CUR_COLOR = grid[r0][c0]
        seen = set()

        def dfs(x, y):
            if (x, y) in seen:
                return 1
            if 0 <= x <= R - 1 and 0 <= y <= C - 1 and grid[x][y] == CUR_COLOR:
                seen.add((x, y))
                cnt = dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
                if cnt < 4:
                    grid[x][y] = color
                return 1
            return 0

        dfs(r0, c0)
        return grid


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        grid=[[1, 1], [1, 2]], r0=0, c0=0, color=3
    ), [[3, 3], [3, 2]]),
    pytest.param(dict(grid=[[1, 2, 2], [2, 3, 2]], r0=0, c0=1, color=3), [[1, 3, 3], [2, 3, 3]]),
    pytest.param(dict(grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], r0=1, c0=1, color=2), [[2, 2, 2], [2, 1, 2], [2, 2, 2]]),
])
def test_solutions(kwargs, expected):
    kw1 = copy.deepcopy(kwargs)
    assert Solution().colorBorder(**kwargs) == expected
    assert Solution1().colorBorder(**kw1) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
