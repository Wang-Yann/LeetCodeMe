#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们将石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。 
# 
#  每次 move 操作都会移除一块所在行或者列上有其他石头存在的石头。 
# 
#  请你设计一个算法，计算最多能执行多少次 move 操作？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
#  
# 
#  示例 2： 
# 
#  输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：stones = [[0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 1000 
#  0 <= stones[i][j] < 10000 
#  
#  Related Topics 深度优先搜索 并查集

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = self.find_set(x), self.find_set(y)
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution(object):
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        对于一个坐标为 (i, j) 的石子来说，需要把行 i 和列 j 合并，因为并查集是一维的，用 j+10000 来代替 j
        """
        MAX_ROW = 10000
        union_find = UnionFind(2 * MAX_ROW)
        for r, c in stones:
            union_find.union_set(r, c + MAX_ROW)
        return len(stones) - len({union_find.find_set(r) for r, _ in stones})


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def removeStones(self, stones: List[List[int]]) -> int:
        cols_set = collections.defaultdict(list)
        rows_set = collections.defaultdict(list)
        for idx, (r, c) in enumerate(stones):
            rows_set[r].append(idx)
            cols_set[c].append(idx)
        N = len(stones)
        uf = UnionFind(N)
        for r, idxs in rows_set.items():
            for i in range(1, len(idxs)):
                uf.union_set(idxs[0], idxs[i])
        for c, idxs in cols_set.items():
            for i in range(1, len(idxs)):
                uf.union_set(idxs[0], idxs[i])
        left_set = set(uf.find_set(x) for x in uf.set)
        # print(uf.set, left_set)
        return N - len(left_set)


@pytest.mark.parametrize("kw,expected", [
    [dict(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]), 5],
    [dict(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3],
    [dict(stones=[[0, 0]]), 0],
    [dict(stones=[[0, 1], [1, 0], [1, 1]]), 2],
])
def test_solutions(kw, expected):
    assert Solution().removeStones(**kw) == expected
    assert Solution1().removeStones(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
