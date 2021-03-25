#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 N 个网络节点，标记为 1 到 N。 
# 
#  给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从
# 源节点传递到目标节点的时间。 
# 
#  现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# 输出：2
#  
# 
#  
# 
#  注意: 
# 
#  
#  N 的范围在 [1, 100] 之间。 
#  K 的范围在 [1, N] 之间。 
#  times 的长度在 [1, 6000] 之间。 
#  所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。 
#  
#  Related Topics 堆 深度优先搜索 广度优先搜索 图

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        堆优化的Dijkstra's
        """
        graph = collections.defaultdict(list)
        for u, v, weight in times:
            graph[u].append((v, weight))
        pq = [(0, K)]
        dist = {}
        # use a heap to store the nodes that may generate the next node with shortest distance
        while pq:
            distance, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = distance
            for neighbor, distance2 in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (distance + distance2, neighbor))
        return max(dist.values()) if len(dist) == N else -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Dijkstra's
        """
        graph = collections.defaultdict(list)
        for u, v, weight in times:
            graph[u].append((v, weight))
        dist = {node:float("inf") for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0
        while True:
            cand_node = -1
            cand_dist = float("inf")
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            if cand_node < 0:
                break
            seen[cand_node] = True
            for neighbor, d in graph[cand_node]:
                dist[neighbor] = min(dist[neighbor], dist[cand_node] + d)
        ans = max(dist.values())
        return ans if ans < float("inf") else -1


@pytest.mark.parametrize("kwargs,expected", [
    (dict(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().networkDelayTime(**kwargs) == expected
    assert Solution1().networkDelayTime(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
