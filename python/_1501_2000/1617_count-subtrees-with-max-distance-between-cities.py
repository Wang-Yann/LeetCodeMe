#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 07:46:21
# @Last Modified : 2021-02-22 07:46:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和
#  vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。 
# 
#  一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另
# 一棵子树中不存在。 
# 
#  对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。 
# 
#  请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。 
# 
#  请注意，两个城市间距离定义为它们之间需要经过的边的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 4, edges = [[1,2],[2,3],[2,4]]
# 输出：[3,4,0]
# 解释：
# 子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
# 子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
# 不存在城市间最大距离为 3 的子树。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2, edges = [[1,2]]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 3, edges = [[1,2],[2,3]]
# 输出：[2,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 15 
#  edges.length == n-1 
#  edges[i].length == 2 
#  1 <= ui, vi <= n 
#  题目保证 (ui, vi) 所表示的边互不相同。 
#  
#  Related Topics 回溯算法 
#  👍 24 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        树形DP
        题目难度超标了吧
        """

        def bfs(src, cities):
            visited = {src}
            q = collections.deque([(src, 0)])  # Pair of (vertex, distance)
            farthest_dist = 0  # Farthest distance from src to other nodes
            while len(q) > 0:
                u, d = q.popleft()
                farthest_dist = d
                for v in graph[u]:
                    if v not in visited and v in cities:
                        visited.add(v)
                        q.append((v, d + 1))
            return farthest_dist, visited

        def maxDistance(cur_state):  # return: maximum distance between any two cities in our subset. O(n^2)
            cities = set()
            for i in range(n):
                if (cur_state >> i) & 1 == 1:
                    cities.add(i)
            res = 0
            for i in cities:
                farthest_dist, visited = bfs(i, cities)
                if len(visited) < len(cities):
                    return 0  # Can't visit all nodes of the tree -> Invalid tree
                res = max(res, farthest_dist)
            return res

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        ans = [0] * (n - 1)
        for state in range(1, 2 ** n):
            d = maxDistance(state)
            if d > 0:
                ans[d - 1] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(n=4, edges=[[1, 2], [2, 3], [2, 4]]), [3, 4, 0]],
    [dict(n=2, edges=[[1, 2]]), [1]],
    [dict(n=3, edges=[[1, 2], [2, 3]]), [2, 1]],
])
def test_solutions(kw, expected):
    assert Solution().countSubgraphsForEachDiameter(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
