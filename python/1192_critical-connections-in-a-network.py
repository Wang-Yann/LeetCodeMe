#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。 
# 
#  它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。 
# 
#  从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器
# 。 
# 
#  「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。 
# 
#  请你以任意顺序返回该集群内的所有 「关键连接」。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  n-1 <= connections.length <= 10^5 
#  connections[i][0] != connections[i][1] 
#  不存在重复的连接 
#  
#  Related Topics 深度优先搜索

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        TODO TODO
        An edge is a critical connection, if and only if it is not in a cycle.
        Tarjan Algorithm (DFS) Python Solution with explanation

        """

        graph = collections.defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        INT_MAX = 0x7fffffff
        dfn = [INT_MAX for _ in range(n)]
        low = [INT_MAX for _ in range(n)]

        res = []
        self.cur = 0

        def dfs(node, parent):
            if dfn[node] == INT_MAX:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for neighbor in graph[node]:
                    if dfn[neighbor] == INT_MAX:
                        dfs(neighbor, node)

                if parent is not None:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    l = min(low[i] for i in graph[node] + [low[node]])
                low[node] = l

        dfs(0, None)
        # print(low,dfn)
        for v in connections:
            if low[v[0]] > dfn[v[1]] or low[v[1]] > dfn[v[0]]:
                res.append(v)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]), ([[1, 3]], [[3, 1]])],
])
def test_solutions(kw, expected):
    assert Solution().criticalConnections(**kw) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
