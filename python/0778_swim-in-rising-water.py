#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 21:10:34
# @Last Modified : 2020-05-02 21:10:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
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
