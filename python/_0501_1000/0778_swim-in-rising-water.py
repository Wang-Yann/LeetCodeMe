#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 21:10:34
# @Last Modified : 2020-05-02 21:10:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
#
#  现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两
# 个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
#
#  你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
#
#
#
#  示例 1:
#
#  输入: [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
#
# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
#
#
#  示例2:
#
#  输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,
# 6]]
# 输出: 16
# 解释:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
#
# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
#
#
#
#
#  提示:
#
#
#  2 <= N <= 50.
#  grid[i][j] 位于区间 [0, ..., N*N - 1] 内。
#
#  Related Topics 堆 深度优先搜索 并查集 二分查找
#  👍 51 👎 0

"""

import heapq
from typing import List

import pytest

from common_utils import UnionFind


class Solution:
    """并查集"""

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        positions = [None] * (n ** 2)
        for i in range(n):
            for j in range(n):
                positions[grid[i][j]] = (i, j)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        uf = UnionFind(n ** 2)
        for elevation in range(n ** 2):
            i, j = positions[elevation]
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x <= (n - 1) and 0 <= y <= (n - 1) and grid[x][y] <= elevation:
                    uf.union_set(i * n + j, x *n+y)
                    if uf.find(0) == uf.find(n ** 2 - 1):
                        return elevation
        return n ** 2 - 1


class Solution1(object):
    def swimInWater(self, grid):
        """BFS"""
        N = len(grid)

        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            elevation, row, col = heapq.heappop(pq)
            ans = max(ans, elevation)
            if row == col == N-1: return ans
            for c_row, c_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0 <= c_row < N and 0 <= c_col < N and (c_row, c_col) not in seen:
                    heapq.heappush(pq, (grid[c_row][c_col], c_row, c_col))
                    seen.add((c_row, c_col))

@pytest.mark.parametrize("grid,expected", [
    ([[0, 2], [1, 3]], 3),
    pytest.param([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
])
def test_solutions(grid, expected):
    assert Solution().swimInWater(grid) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
