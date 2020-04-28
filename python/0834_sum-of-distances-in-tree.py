#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:54:30
# @Last Modified : 2020-04-24 16:54:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from typing import List


class Solution:
    def sumOfDistancesInTreeMe(self, N: int, edges: List[List[int]]) -> List[int]:
        """超出时间限制"""
        if not N: return []
        if not edges: return [0]
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

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        官方解法
        https://leetcode-cn.com/problems/sum-of-distances-in-tree/solution/shu-zhong-ju-chi-zhi-he-by-leetcode/
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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(N=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]),
        dict(N=1, edges=[])

    ]
    lists = [x for x in samples]
    res = [sol.sumOfDistancesInTree(**x) for x in lists]
    print(res)
