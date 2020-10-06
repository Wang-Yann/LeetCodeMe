#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:54:30
# @Last Modified : 2020-04-24 16:54:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
#
#  第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
#
#  返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
#
#  示例 1:
#
#
# 输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释:
# 如下为给定的树的示意图：
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
#
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
#
#
#  说明: 1 <= N <= 10000
#  Related Topics 树 深度优先搜索
#  👍 85 👎 0


import collections
from typing import List

import pytest


class Solution0:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """Me超出时间限制 TLE"""
        if not N:
            return []
        if not edges:
            return [0]
        v_map = collections.defaultdict(list)
        for s, d in edges:
            v_map[s].append(d)
            v_map[d].append(s)

        results = []

        for s in range(N):
            is_visited = set()
            level = 1
            ans = 0
            dq = [s]
            while dq:
                length = len(dq)
                for i in range(length):
                    val = dq.pop(0)
                    for v in v_map[val]:
                        if v in is_visited:
                            continue
                        ans += level
                        dq.append(v)
                    is_visited.add(val)
                level += 1
            results.append(ans)
        return results


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        官方解法
        https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)

        Let's solve it with node 0 as root.

        Initial an array of hashset tree, tree[i] contains all connected nodes to i.
        Initial an array count, count[i] counts all nodes in the subtree i.
        Initial an array of res, res[i] counts sum of distance in subtree i.

        Post order dfs traversal, update count and res:
        count[root] = sum(count[i]) + 1
        res[root] = sum(res[i]) + sum(count[i])

        Pre order dfs traversal, update res:
        When we move our root from parent to its child i, count[i] points get 1 closer to root, n - count[i] nodes get 1 futhur to root.
        res[i] = res[root] - count[i] + N - count[i]

        return res, done.
        深度优先搜索 + 子树计数
        """
        graph = collections.defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        count = [1] * N
        ans = [0] * N

        def dfs(cur, parent):
            for child in graph[cur]:
                if child != parent:
                    dfs(child, cur)
                    count[cur] += count[child]
                    ans[cur] += ans[child] + count[child]

        def dfs2(cur, parent):
            for child in graph[cur]:
                if child != parent:
                    ans[child] = ans[cur] - count[child] + N - count[child]
                    dfs2(child, cur)

        dfs(0, None)
        dfs2(0, None)
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]), [8, 12, 6, 10, 10, 10]],
    [dict(N=1, edges=[]), [0]],
])
def test_solutions(kw, expected):
    assert Solution().sumOfDistancesInTree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
