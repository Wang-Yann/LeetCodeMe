#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 11:03:10
# @Last Modified : 2020-04-20 11:03:10
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集
#  👍 658 👎 0


from typing import List

from common_utils import UnionFindGrid as   UnionFind


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "0":
                    continue
                for dlt_x, dlt_y in directions:
                    x, y = r + dlt_x, c + dlt_y
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        uf.union(r * n + c, x * n + y)
        return uf.getCout()

    def numIslandsMe(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = "0"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dlt_x, dlt_y in directions:
                x, y = i + dlt_x, j + dlt_y
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 \
                        and grid[x][y] == "1":
                    dfs(x, y)

        if not grid: return 0
        m, n = len(grid), len(grid[0])
        cnt_of_dfs = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    dfs(row, col)
                    cnt_of_dfs += 1
        return cnt_of_dfs


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["1", "0", "1", "0", "0"]
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]

    ]
    lists = [x for x in samples]
    res = [sol.numIslands(x) for x in lists]
    print(res)
