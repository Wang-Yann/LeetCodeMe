#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:34:26
# @Last Modified : 2020-08-04 17:34:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 想象一下你是个城市基建规划者，地图上有 N 座城市，它们按以 1 到 N 的次序编号。 
# 
#  给你一些可连接的选项 conections，其中每个选项 conections[i] = [city1, city2, cost] 表示将城市 city1
#  和城市 city2 连接所要的成本。（连接是双向的，也就是说城市 city1 和城市 city2 相连也同样意味着城市 city2 和城市 city1 相连）
# 。 
# 
#  返回使得每对城市间都存在将它们连接在一起的连通路径（可能长度为 1 的）最小成本。该最小成本应该是所用全部连接代价的综合。如果根据已知条件无法完成该项任务
# ，则请你返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：N = 3, conections = [[1,2,5],[1,3,6],[2,3,1]]
# 输出：6
# 解释：
# 选出任意 2 条边都可以连接所有城市，我们从中选取成本最小的 2 条。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：N = 4, conections = [[1,2,3],[3,4,4]]
# 输出：-1
# 解释： 
# 即使连通所有的边，也无法连接所有城市。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10000 
#  1 <= conections.length <= 10000 
#  1 <= conections[i][0], conections[i][1] <= N 
#  0 <= conections[i][2] <= 10^5 
#  conections[i][0] != conections[i][1] 
#  
#  Related Topics 并查集 图 
#  👍 24 👎 0

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))
        self.size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.size -= 1
        return True


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        """AC"""
        uf = UnionFind(N)
        connections.sort(key=lambda x: x[2])
        cost = 0
        for u, v, w in connections:
            if uf.union_set(u - 1, v - 1):
                cost += w
            if uf.size == 1:
                break
        return cost if uf.size == 1 else -1


# leetcode submit region end(Prohibit modification and deletion)

# 最小生成树算法
class Solution1:
    """
    kruskal 算法  ; 基本就是使用并查集
        将所有的边按照权重从小到大排序。
        取一条权重最小的边。
        使用并查集（union-find）数据结构来判断加入这条边后是否会形成环。若不会构成环，则将这条边加入最小生成树中。
        检查所有的结点是否已经全部联通，这一点可以通过目前已经加入的边的数量来判断。若全部联通，则结束算法；否则返回步骤 2.

    """

    def find(self, x):
        if x == self.father[x]:
            return x
        return self.find(self.father[x])

    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        self.father = [i for i in range(N + 1)]
        connections.sort(key=lambda edge: edge[2])
        ans = 0
        edge_cnt = 0
        for a, b, cost in connections:
            root_a = self.find(a)
            root_b = self.find(b)
            if root_a != root_b:
                self.father[root_a] = root_b
                ans += cost
                edge_cnt += 1
            if edge_cnt == N - 1:
                return ans
        return -1


class Solution2:
    """
    Prim算法

        根据 connections 记录每个顶点到其他顶点的权重，记为 G 。
        使用 visited 记录所有被访问过的点。
        使用堆来根据权重比较所有的边。
        将任意一个点记为已访问，并将其所有连接的边放入堆中。
        从堆中拿出权重最小的边。
        如果已经访问过，直接丢弃。
        如果未访问过，标记为已访问，并且将其所有连接的边放入堆中，检查是否有 N 个点。
        重复操作 5。

    """

    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        G = collections.defaultdict(list)
        for a, b, cost in connections:
            G[a].append((b, cost))
            G[b].append((a, cost))
        seen = set()
        # 存储可以向外扩展的边，格式为（开销，目的城市）
        out_edges = [(0, 1)]
        ans = 0
        while out_edges and len(seen) != N:
            cost, city = heapq.heappop(out_edges)
            if city not in seen:
                seen.add(city)
                ans += cost
                for next_city, next_cost in G[city]:
                    heapq.heappush(out_edges, (next_cost, next_city))
        if len(seen) != N:
            return -1
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(N=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]), 6],
    [dict(N=4, connections=[[1, 2, 3], [3, 4, 4]]), -1],
])
def test_solutions(kw, expected):
    assert Solution().minimumCost(**kw) == expected
    assert Solution1().minimumCost(**kw) == expected
    assert Solution2().minimumCost(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
