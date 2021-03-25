#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-10 08:47:11
# @Last Modified : 2021-03-10 08:47:11
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 现有一个加权无向连通图。给你一个正整数 n ，表示图中有 n 个节点，并按从 1 到 n 给节点编号；另给你一个数组 edges ，其中每个 edges[i
# ] = [ui, vi, weighti] 表示存在一条位于节点 ui 和 vi 之间的边，这条边的权重为 weighti 。 
# 
#  从节点 start 出发到节点 end 的路径是一个形如 [z0, z1, z2, ..., zk] 的节点序列，满足 z0 = start 、zk = 
# end 且在所有符合 0 <= i <= k-1 的节点 zi 和 zi+1 之间存在一条边。 
# 
#  路径的距离定义为这条路径上所有边的权重总和。用 distanceToLastNode(x) 表示节点 n 和 x 之间路径的最短距离。受限路径 为满足 d
# istanceToLastNode(zi) > distanceToLastNode(zi+1) 的一条路径，其中 0 <= i <= k-1 。 
# 
#  返回从节点 1 出发到节点 n 的 受限路径数 。由于数字可能很大，请返回对 109 + 7 取余 的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
# 输出：3
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是：
# 1) 1 --> 2 --> 5
# 2) 1 --> 2 --> 3 --> 5
# 3) 1 --> 3 --> 5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,
# 6,4]]
# 输出：1
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 104 
#  n - 1 <= edges.length <= 4 * 104 
#  edges[i].length == 3 
#  1 <= ui, vi <= n 
#  ui != vi 
#  1 <= weighti <= 105 
#  任意两个节点之间至多存在一条边 
#  任意两个节点之间至少存在一条路径 
#  
#  Related Topics 图 动态规划 
#  👍 25 👎 0


import collections
import functools
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        def dijkstra():  # Dijkstra to find shortest distance of paths from node `n` to any other nodes
            minHeap = [(0, n)]  # dist, node
            dist = [float('inf')] * (n + 1)
            dist[n] = 0
            while minHeap:
                d, u = heapq.heappop(minHeap)
                if d != dist[u]:
                    continue
                for w, v in graph[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(minHeap, (dist[v], v))
            return dist

        @functools.lru_cache(None)
        def dfs(src):
            if src == n:
                return 1  # Found a path to reach to destination
            ans = 0
            for _, nei in graph[src]:
                if dist[src] > dist[nei]:
                    ans = (ans + dfs(nei)) % MOD
            return ans

        MOD = 10 ** 9 + 7
        dist = dijkstra()
        return dfs(1) % MOD
    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=5, edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]), 3],
    [dict(n=7, edges=[[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2], [7, 5, 3], [2, 6, 4]]), 1],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countRestrictedPaths(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
