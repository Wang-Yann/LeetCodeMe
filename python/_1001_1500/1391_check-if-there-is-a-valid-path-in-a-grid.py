#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 m x n 的网格 grid。网格里的每个单元都代表一条街道。grid[i][j] 的街道可以是： 
# 
#  
#  1 表示连接左单元格和右单元格的街道。 
#  2 表示连接上单元格和下单元格的街道。 
#  3 表示连接左单元格和下单元格的街道。 
#  4 表示连接右单元格和下单元格的街道。 
#  5 表示连接左单元格和上单元格的街道。 
#  6 表示连接右单元格和上单元格的街道。 
#  
# 
#  
# 
#  你最开始从左上角的单元格 (0,0) 开始出发，网格中的「有效路径」是指从左上方的单元格 (0,0) 开始、一直到右下方的 (m-1,n-1) 结束的路径
# 。该路径必须只沿着街道走。 
# 
#  注意：你 不能 变更街道。 
# 
#  如果网格中存在有效的路径，则返回 true，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[2,4,3],[6,5,2]]
# 输出：true
# 解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,2,1],[1,2,1]]
# 输出：false
# 解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,1,2]]
# 输出：false
# 解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。
#  
# 
#  示例 4： 
# 
#  输入：grid = [[1,1,1,1,1,1,3]]
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  1 <= grid[i][j] <= 6 
#  
#  Related Topics 深度优先搜索 广度优先搜索

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = {(i, j): (i, j) for i in range(-1, 2 * m) for j in range(-1, 2 * n)}

        def find_set(x):
            if uf[x] != x:
                uf[x] = find_set(uf[x])
            return uf[x]

        def union_set(i, j, di, dj):
            uf[find_set((i, j))] = find_set((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] in [2, 5, 6]:
                    union_set(i * 2, j * 2, -1, 0)
                if grid[i][j] in [1, 3, 5]:
                    union_set(i * 2, j * 2, 0, -1)
                if grid[i][j] in [2, 3, 4]:
                    union_set(i * 2, j * 2, 1, 0)
                if grid[i][j] in [1, 4, 6]:
                    union_set(i * 2, j * 2, 0, 1)
        return find_set((0, 0)) == find_set((2 * (m - 1), 2 * (n - 1)))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        Why (-d[0], -d[1]) in directions[grid[ni][nj]]:?

            When traversing from one cell to the next. the next cell must have a direction that is the opposite of the direction
            we are moving in for the cells to be connected. For example, if we are moving one unit to the right,
            then from the next cell it must be possible to go one unit to the left, otherwise it's not actually connected
        """
        if not grid:
            return True
        directions = {1: [(0, -1), (0, 1)],
                      2: [(-1, 0), (1, 0)],
                      3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)],
                      5: [(0, -1), (-1, 0)],
                      6: [(0, 1), (-1, 0)]}
        visited = set()
        m, n = len(grid), len(grid[0])
        goal = (m - 1, n - 1)

        @functools.lru_cache(None)
        def dfs(i, j):
            visited.add((i, j))
            if (i, j) == goal:
                return True
            for d in directions[grid[i][j]]:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni <= m - 1 and 0 <= nj <= n - 1 \
                        and (ni, nj) not in visited \
                        and (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False

        return dfs(0, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[2, 4, 3], [6, 5, 2]]), True],
    [dict(grid=[[1, 2, 1], [1, 2, 1]]), False],
    [dict(grid=[[1, 1, 2]]), False],
    [dict(grid=[[1, 1, 1, 1, 1, 1, 3]]), True],
    [dict(grid=[[2], [2], [2], [2], [2], [2], [6]]), True],
])
def test_solutions(kw, expected):
    assert Solution().hasValidPath(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
