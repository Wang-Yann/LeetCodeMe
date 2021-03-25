#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们有一系列公交路线。每一条路线 routes[i] 上都有一辆公交车在上面循环行驶。例如，有一条路线 routes[0] = [1, 5, 7]，表示第一
# 辆 (下标为0) 公交车会一直按照 1->5->7->1->5->7->1->... 的车站路线行驶。 
# 
#  假设我们从 S 车站开始（初始时不在公交车上），要去往 T 站。 期间仅可乘坐公交车，求出最少乘坐的公交车数量。返回 -1 表示不可能到达终点车站。 
# 
#  
# 示例:
# 输入: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# 输出: 2
# 解释: 
# 最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6。
#  
# 
#  说明: 
# 
#  
#  1 <= routes.length <= 500. 
#  1 <= routes[i].length <= 500. 
#  0 <= routes[i][j] < 10 ^ 6. 
#  
#  Related Topics 广度优先搜索

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):

    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        routes = list(map(set, routes))
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route:
                seen.add(node)
            if T in route:
                targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets:
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1


# leetcode submit region end(Prohibit modification and deletion)

class SolutionTLE:

    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        我们需要知道从一个站可以乘坐哪些巴士, 这一点可以用一个哈希表 (HashMap/map/dict) 来记录.
然后从起点开始 BFS, 记录到达每个站点所需要乘坐的最少的巴士数量即可. 注意不要重复乘坐某一辆巴士或者重复到达某一个站点
        """
        if S == T:
            return 0
        to_route = collections.defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                to_route[stop].append(i)
        lookup = {S}
        res = 1
        pq = [S]
        while pq:
            next_q = []
            for stop in pq:
                for i in to_route[stop]:
                    for next_stop in routes[i]:
                        if next_stop in lookup:
                            continue
                        if next_stop == T:
                            return res
                        next_q.append(next_stop)
                        to_route[next_stop].remove(i)
                        lookup.add(next_stop)
            pq = next_q
            res += 1
        return -1


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        routes=[[1, 2, 7], [3, 6, 7]],
        S=1,
        T=6
    ), 2),
    # 问题用例
    (dict(
        routes=[[2], [2, 8]],
        S=8,
        T=2
    ), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().numBusesToDestination(**kwargs) == expected
    assert SolutionTLE().numBusesToDestination(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
