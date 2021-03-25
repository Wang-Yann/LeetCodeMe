#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 23:07:43
# @Last Modified : 2020-07-16 23:07:43
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 
# 的一条无向边，且该边遍历成功的概率为 succProb[i] 。 
# 
#  指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。 
# 
#  如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, e
# nd = 2
# 输出：0.25000
# 解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, e
# nd = 2
# 输出：0.30000
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# 输出：0.00000
# 解释：节点 0 和 节点 2 之间不存在路径
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 10^4 
#  0 <= start, end < n 
#  start != end 
#  0 <= a, b < n 
#  a != b 
#  0 <= succProb.length == edges.length <= 2*10^4 
#  0 <= succProb[i] <= 1 
#  每两个节点之间最多有一条边 
#  
#  Related Topics 图 
#  👍 14 👎 0


"""
import collections
import heapq
from typing import List

import pytest


# """TLE"""
# graph = collections.defaultdict(list)
# for [a, b], w in zip(edges, succProb):
#     graph[a].append((b, w))
#     graph[b].append((a, w))
# self.ans = 0
#
# def dfs(node, p, seen):
#     if node == end:
#         self.ans = max(self.ans, p)
#         return
#     for neighbor, w in graph[node]:
#         if neighbor not in seen:
#             dfs(neighbor, p * w, seen | {neighbor})
#
# dfs(start, 1, {start})
# return self.ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        Dijkstra
        TODO
        """
        p, G = [0.0] * n, collections.defaultdict(list)
        for index, (a, b) in enumerate(edges):
            G[a].append((b, index))
            G[b].append((a, index))
        p[start] = 1.0
        heap = [(-p[start], start)]
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neighbor, index in G[cur]:
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        return 0.0


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """Bellman Ford"""
        G, dq = collections.defaultdict(list), collections.deque([start])
        for i, (a, b) in enumerate(edges):
            G[a].append([b, i])
            G[b].append([a, i])
        p = [0.0] * n
        p[start] = 1.0
        while dq:
            cur = dq.popleft()
            for neighbor, i in G[cur]:
                if p[cur] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[cur] * succProb[i]
                    dq.append(neighbor)
        return p[end]


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2), 0.25],

    pytest.param(dict(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2), 0.3),
    pytest.param(dict(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2), 0.0),
])
def test_solutions(kwargs, expected):
    res = Solution().maxProbability(**kwargs)
    res1 = Solution().maxProbability(**kwargs)
    assert res == pytest.approx(expected, 1e-5)
    assert res1 == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
