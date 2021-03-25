#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 从具有 0 到 N-1 的结点的无向图（“原始图”）开始，对一些边进行细分。 
# 
#  该图给出如下：edges[k] 是整数对 (i, j, n) 组成的列表，使 (i, j) 是原始图的边。 
# 
#  n 是该边上新结点的总数 
# 
#  然后，将边 (i, j) 从原始图中删除，将 n 个新结点 (x_1, x_2, ..., x_n) 添加到原始图中， 
# 
#  将 n+1 条新边 (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) 添加到
# 原始图中。 
# 
#  现在，你将从原始图中的结点 0 处出发，并且每次移动，你都将沿着一条边行进。 
# 
#  返回最多 M 次移动可以达到的结点数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
# 输出：13
# 解释：
# 在 M = 6 次移动之后在最终图中可到达的结点如下所示。
# 
#  
# 
#  示例 2： 
# 
#  输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
# 输出：23 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= edges.length <= 10000 
#  0 <= edges[i][0] < edges[i][1] < N 
#  不存在任何 i != j 情况下 edges[i][0] == edges[j][0] 且 edges[i][1] == edges[j][1]. 
#  原始图没有平行的边。 
#  0 <= edges[i][2] <= 10000 
#  0 <= M <= 10^9 
#  1 <= N <= 3000 
#  可到达结点是可以从结点 0 开始使用最多 M 次移动到达的结点。 
#  
# 
#  
#  Related Topics 堆

"""

import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        """
        Dijkstra
        对于每条（有向）边 (node，nei)，我们将跟踪有多少新结点（从原始边细分而来的新结点）被使用。 最后，我们将总结每条边的利用率。
        假设我们现在把每个添加的节点看作为一个单位距离，那这不就是从0点出发，每条路径最多走M个单位距离，问我们能够经过多少个不同的单位距离
        """
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        pq = [(0, 0)]
        dist = {0:0}
        used = {}
        ans = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1
            for neighbor, weight in graph[node].items():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # wei is the maximum utilization of this edge
                wei = min(weight, M - d)
                used[node, neighbor] = wei
                # d2 is the total distance to reach 'nei' (nei***or) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(neighbor, M + 1):
                    heapq.heappush(pq, (d2, neighbor))
                    dist[neighbor] = d2
        # print(used,dist)
        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], M=6, N=3
    ), 13),
    pytest.param(dict(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], M=10, N=4), 23),
])
def test_solutions(kwargs, expected):
    assert Solution().reachableNodes(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
