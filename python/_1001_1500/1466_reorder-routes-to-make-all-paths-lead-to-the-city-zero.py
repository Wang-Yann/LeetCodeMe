#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 14:51:12
# @Last Modified : 2020-07-10 14:51:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输
# 部决定重新规划路线，以改变交通拥堵的状况。 
# 
#  路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。 
# 
#  今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。 
# 
#  请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。 
# 
#  题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# 输出：3
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。 
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# 输出：2
# 解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。 
# 
#  示例 3： 
# 
#  输入：n = 3, connections = [[1,0],[2,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 5 * 10^4 
#  connections.length == n-1 
#  connections[i].length == 2 
#  0 <= connections[i][0], connections[i][1] <= n-1 
#  connections[i][0] != connections[i][1] 
#  
#  Related Topics 树 深度优先搜索 
#  👍 27 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        GOOD
        Start from node 0 (the capital) and dfs on the path and see if the path is
        in the same direction as the traversal. If it is on the same direction that
        means we need to reverse it because it can never get to the capital.
        """
        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node, parent):
            if (parent, node) in roads:
                self.res += 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        dfs(0, -1)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3],
    [dict(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]), 2],
    [dict(n=3, connections=[[1, 0], [2, 0]]), 0],
])
def test_solutions(kw, expected):
    assert Solution().minReorder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
