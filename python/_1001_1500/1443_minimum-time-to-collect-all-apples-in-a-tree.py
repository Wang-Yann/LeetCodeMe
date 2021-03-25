#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 23:32:29
# @Last Modified : 2020-07-09 23:32:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最
# 少需要多少秒，可以收集到所有苹果，并回到节点 0 。 
# 
#  无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数
# 组 hasApple ，其中 hasApple[i] = True 代表节点 i 有一个苹果，否则，节点 i 没有苹果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,fa
# lse,True,False,True,True,False]
# 输出：8 
# 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,fa
# lse,True,False,False,True,False]
# 输出：6
# 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。
#  
# 
#  示例 3： 
# 
#  输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,fa
# lse,False,False,False,False,False]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  edges.length == n-1 
#  edges[i].length == 2 
#  0 <= fromi, toi <= n-1 
#  fromi < toi 
#  hasApple.length == n 
#  
#  Related Topics 树 深度优先搜索 
#  👍 26 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        GOOD
        如果一个点的子节点ans大于0,则说明摘时必经此子树，因此本节点ans需要+2
        如果一个点的子节点ans等于0,并且此节点为true,则说明摘时需要经过此子节点，本节点ans需要+2

        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            secs = 0
            for child in graph[node]:
                secs += dfs(child)
            if secs > 0:
                return secs + 2
            return 2 if hasApple[node] else 0

        # Root
        return max(dfs(0) - 2, 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, True, True, False]), 8],
    pytest.param(
        dict(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, False, True, False]), 6),
    pytest.param(
        dict(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, False, False, False, False, False]), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minTime(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
