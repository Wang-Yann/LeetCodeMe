#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-03 10:54:32
# @Last Modified : 2020-08-03 10:54:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定有向图的边 edges，以及该图的始点 source 和目标终点 destination，确定从始点 source 出发的所有路径是否最终结束于目标终点
#  destination，即： 
# 
#  
#  从始点 source 到目标终点 destination 存在至少一条路径 
#  如果存在从始点 source 到没有出边的节点的路径，则该节点就是路径终点。 
#  从始点source到目标终点 destination 可能路径数是有限数字 
#  
# 
#  当从始点 source 出发的所有路径都可以到达目标终点 destination 时返回 true，否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
# 输出：false
# 说明：节点 1 和节点 2 都可以到达，但也会卡在那里。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
# 输出：false
# 说明：有两种可能：在节点 3 处结束，或是在节点 1 和节点 2 之间无限循环。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
# 输出：true
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
# 输出：false
# 说明：从始点出发的所有路径都在目标终点结束，但存在无限多的路径，如 0-1-2，0-1-1-2，0-1-1-1-2，0-1-1-1-1-2 等。
#  
# 
#  示例 5： 
# 
#  
# 
#  输入：n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
# 输出：false
# 说明：在目标节点上存在无限的自环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的图中可能带有自环和平行边。 
#  图中的节点数 n 介于 1 和 10000 之间。 
#  图中的边数在 0 到 10000 之间。 
#  0 <= edges.length <= 10000 
#  edges[i].length == 2 
#  0 <= source <= n - 1 
#  0 <= destination <= n - 1 
#  
#  Related Topics 深度优先搜索 图 
#  👍 14 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if not G[node]:
                return node == destination
            for neighbor in G[node]:
                #  判断是否有环 并 递归子节点
                if visited[neighbor]:
                    return False
                visited[neighbor] = True
                if not dfs(neighbor, visited):
                    return False
                visited[neighbor] = False
            return True

        G = collections.defaultdict(list)
        for s, e in edges:
            G[s].append(e)
        if G[destination]:
            return False
        return dfs(source, [False] * n)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, edges=[[0, 1], [0, 2]], source=0, destination=2), False],
    [dict(n=4, edges=[[0, 1], [0, 3], [1, 2], [2, 1]], source=0, destination=3), False],
    [dict(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]], source=0, destination=3), True],
    [dict(n=3, edges=[[0, 1], [1, 1], [1, 2]], source=0, destination=2), False],
    [dict(n=2, edges=[[0, 1], [1, 1]], source=0, destination=1), False],
])
def test_solutions(kw, expected):
    assert Solution().leadsToDestination(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
