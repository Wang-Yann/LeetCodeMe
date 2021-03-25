#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 16:30:28
# @Last Modified : 2020-07-27 16:30:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。 
# 
#  示例 1: 
# 
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
# 
#      0          3
#      |          |
#      1 --- 2    4 
# 
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
#      0           4
#      |           |
#      1 --- 2 --- 3
# 
# 输出:  1
#  
# 
#  注意: 
# 你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0] 相同，所以它们不会同时在 edges 中出现。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 
#  👍 33 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, max_size):
        self.set = list(range(max_size))
        self.count = max_size

    def find_set(self, x):
        if x != self.set[x]:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.count -= 1
        return True


class Solution:
    """AC"""

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union_set(u, v)
        return uf.count


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(n=5, edges=[[0, 1], [1, 2], [3, 4]]), 2],
    [dict(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]), 1],
])
def test_solutions(kw, expected):
    assert Solution().countComponents(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
