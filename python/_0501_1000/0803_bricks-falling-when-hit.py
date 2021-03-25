#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们有一组包含1和0的网格；其中1表示砖块。 当且仅当一块砖直接连接到网格的顶部，或者它至少有一块相邻（4 个方向之一）砖块不会掉落时，它才不会落下。 
# 
#  我们会依次消除一些砖块。每当我们消除 (i, j) 位置时， 对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这个消除而落下。 
# 
#  返回一个数组表示每次消除操作对应落下的砖块数目。 
# 
#  示例 1：
# 输入：
# grid = [[1,0,0,0],[1,1,1,0]]
# hits = [[1,0]]
# 输出: [2]
# 解释: 
# 如果我们消除(1, 0)位置的砖块, 在(1, 1) 和(1, 2) 的砖块会落下。所以我们应该返回2。 
# 
#  示例 2：
# 输入：
# grid = [[1,0,0,0],[1,1,0,0]]
# hits = [[1,1],[1,0]]
# 输出：[0,0]
# 解释：
# 当我们消除(1, 0)的砖块时，(1, 1)的砖块已经由于上一步消除而消失了。所以每次消除操作不会造成砖块落下。注意(1, 0)砖块不会记作落下的砖块。 
# 
#  注意: 
# 
#  
#  网格的行数和列数的范围是[1, 200]。 
#  消除的数字不会超过网格的区域。 
#  可以保证每次的消除都不相同，并且位于网格的内部。 
#  一个消除的位置可能没有砖块，如果这样的话，就不会有砖块落下。 
#  
#  Related Topics 并查集

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, max_size):
        self.set = list(range(max_size + 1))
        self.size = [1] * (max_size + 1)
        self.size[-1] = 0

    def find_set(self, x):
        if x != self.set[x]:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.size[max(x_root, y_root)] += self.size[min(x_root, y_root)]
        return True

    def top(self):
        return self.size[self.find_set(len(self.size) - 1)]


class Solution:

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        """
        首先我们添加一个虚拟的节点，它的编号为 R * C（网格中的节点编号为 [0, R * C - 1]），代表网格的顶部，任何第一行的砖块都会与它相连

        我们可以倒着思考: 首先把 hits 内所有指定的砖块打掉 (注意区分对应位置初始到底有没有砖块), 然后倒着一步一步恢复. 每当我们恢复一个砖块,
        查看他四周的砖块, 有可能与底部连接着, 也有可能没有连接.

        如果恢复一个砖块, 它四周连接着的砖块共有 x 块没有与底部相连(算上联通着的所有砖块), 同时也有某一块与底部相连, 或者恢复的这块就在底部,
         那么说明恢复这一块将那 x 块与底部连接起来了. 就是说原本打掉这一块的时候, 会有 x 块掉落.

        在这个过程中我们只关心一个砖块与另一个砖块是否属于同一个联通块, 一个砖块是否与底部属于同一个联通块, 一个联通块的大小, 两个联通块之间和合并.
        这些操作可以由并查集高效完成.

        """

        def index(COLS, r_idx, c_idx):
            return r_idx * COLS + c_idx

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        R, C = len(grid), len(grid[0])

        hit_grid = [row[:] for row in grid]
        for i, j in hits:
            hit_grid[i][j] = 0
        uf = UnionFind(R * C)
        for r, row in enumerate(hit_grid):
            for c, val in enumerate(row):
                if not val:
                    continue
                if r == 0:
                    uf.union_set(index(C, r, c), R * C)
                if r and hit_grid[r - 1][c]:
                    uf.union_set(index(C, r, c), index(C, r - 1, c))
                if c and hit_grid[r][c - 1]:
                    uf.union_set(index(C, r, c), index(C, r, c - 1))
        res = []
        for r, c in reversed(hits):
            prev_roof = uf.top()
            if grid[r][c] == 0:
                res.append(0)
                continue
            for x, y in directions:
                nr, nc = r + x, c + y
                if 0 <= nr <= R - 1 and 0 <= nc <= C - 1 and hit_grid[nr][nc]:
                    uf.union_set(index(C, r, c), index(C, nr, nc))
            if r == 0:
                uf.union_set(index(C, r, c), R * C)
            hit_grid[r][c] = 1
            # print(uf.size,uf.top())
            res.append(max(0, uf.top() - prev_roof - 1))
        return res[::-1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        grid=[[1, 0, 0, 0], [1, 1, 1, 0]],
        hits=[[1, 0]]
    ), [2]),
    pytest.param(dict(
        grid=[[1, 0, 0, 0], [1, 1, 0, 0]],
        hits=[[1, 1], [1, 0]]
    ), [0, 0]),
])
def test_solutions(kwargs, expected):
    assert Solution().hitBricks(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
