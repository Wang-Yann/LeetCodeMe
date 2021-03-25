#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 16:50:32
# @Last Modified : 2020-07-22 16:50:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。 
# 
#  示例 1： 
# 
#  输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true 
# 
#  示例 2: 
# 
#  输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false 
# 
#  注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表 edg
# es 中。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 
#  👍 42 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dq = collections.deque([0])
        seen = {0}
        while dq:
            node = dq.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dq.append(neighbor)
                    seen.add(neighbor)
        return len(seen) == n


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]), True],
    [dict(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False],
])
def test_solutions(kw, expected):
    assert Solution().validTree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
