#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 00:56:30
# @Last Modified : 2020-07-06 00:56:30
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，其中 edges[i] = [fromi, toi, we
# ighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权
# 值和最小。 
# 
#  请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在
# 某些最小生成树中但不会出现在所有最小生成树中的边。 
# 
#  请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# 输出：[[0,1],[2,3,4,5]]
# 解释：上图描述了给定图。
# 下图是所有的最小生成树。
# 
# 注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
# 边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。
#  
# 
#  示例 2 ： 
# 
#  
# 
#  输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# 输出：[[],[0,1,2,3]]
# 解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  1 <= edges.length <= min(200, n * (n - 1) / 2) 
#  edges[i].length == 3 
#  0 <= fromi < toi < n 
#  1 <= weighti <= 1000 
#  所有 (fromi, toi) 数对都是互不相同的。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 10 👎 0

"""
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        self.count -= 1
        return True


class Solution:

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        最小生成树
        """

        def MST(n, edges, unused=None, used=None):
            union_find = UnionFind(n)
            weight = 0
            if used is not None:
                u, v, w, _ = edges[used]
                if union_find.union_set(u, v):
                    weight += w
            for idx, (u, v, w, _) in enumerate(edges):
                if idx == unused:
                    continue
                if union_find.union_set(u, v):
                    weight += w
            return weight if union_find.count == 1 else math.inf

        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x:x[2])
        mst = MST(n, edges)
        result = [[], []]
        for i, (u, v, w, idx) in enumerate(edges):
            # print(i,(u,v,w,idx))
            if mst < MST(n, edges, unused=i):
                result[0].append(idx)
            elif mst == MST(n, edges, used=i):
                result[1].append(idx)
        return result


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=5, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]), [[0, 1], [2, 3, 4, 5]]),
    pytest.param(dict(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]), [[], [0, 1, 2, 3]]),
    pytest.param(dict(n=6, edges=[[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2], [4, 5, 2]]), [[3], [0, 1, 2, 4, 5, 6]]),
])
def test_solutions(kwargs, expected):
    assert Solution().findCriticalAndPseudoCriticalEdges(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
