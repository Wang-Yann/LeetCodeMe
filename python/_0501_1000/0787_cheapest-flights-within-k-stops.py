#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。 
# 
#  现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样
# 的路线，则输出 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。 
# 
#  示例 2： 
# 
#  输入: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# 输出: 500
# 解释: 
# 城市航班图如下
# 
# 
# 从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。 
# 
#  
# 
#  提示： 
# 
#  
#  n 范围是 [1, 100]，城市标签从 0 到 n - 1. 
#  航班数量范围是 [0, n * (n - 1) / 2]. 
#  每个航班的格式 (src, dst, price). 
#  每个航班的价格范围是 [1, 10000]. 
#  k 范围是 [0, n - 1]. 
#  航班没有重复，且不存在环路 
#  
#  Related Topics 堆 广度优先搜索 动态规划

"""
import collections
import heapq
import sys
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Dijkstra
        Not Simple TODO
        """
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K + 1 or cost > best.get((k, place), float("inf")):
                continue
            if place == dst:
                return cost
            for neighbor, wt in graph[place]:
                newcost = cost + wt
                if newcost < best.get((k + 1, neighbor), float("inf")):
                    heapq.heappush(pq, (newcost, k + 1, neighbor))
                    best[k + 1, neighbor] = newcost
        return -1


# leetcode submit region end(Prohibit modification and deletion)
class Solution9:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Bellman-Ford
        # 直接把最短路数组复制一遍, 用副本保存松弛的结果, 也可以保证每一轮迭代最多增加一条边, 不过执行效率略低

        """
        distance = [sys.maxsize for _ in range(n)]
        distance[src] = 0
        for i in range(0, K + 1):
            d_new = list(distance)
            for u, v, c in flights:
                d_new[v] = min(d_new[v], distance[u] + c)
            distance = d_new
        if distance[dst] != sys.maxsize:
            return distance[dst]
        return -1


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        src=0, dst=2, K=1
    ), 200),
    (dict(
        n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        src=0, dst=2, K=0
    ), 500),
])
def test_solutions(kwargs, expected):
    assert Solution().findCheapestPrice(**kwargs) == expected
    assert Solution9().findCheapestPrice(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
