#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 公司共有 n 个项目和 m 个小组，每个项目要不没有归属，要不就由其中的一个小组负责。 
# 
#  我们用 group[i] 代表第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的） 
# 
# 
#  请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表： 
# 
#  
#  同一小组的项目，排序后在列表中彼此相邻。 
#  项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个
# 项目左侧）应该完成的所有项目。 
#  
# 
#  结果要求： 
# 
#  如果存在多个解决方案，只需要返回其中任意一个即可。 
# 
#  如果没有合适的解决方案，就请返回一个 空列表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],
# [3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
#  
# 
#  示例 2： 
# 
#  输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],
# [3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= n <= 3*10^4 
#  group.length == beforeItems.length == n 
#  -1 <= group[i] <= m-1 
#  0 <= beforeItems[i].length <= n-1 
#  0 <= beforeItems[i][j] <= n-1 
#  i != beforeItems[i][j] 
#  
#  Related Topics 深度优先搜索 图 拓扑排序

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        拓扑排序
        topological sorting
        https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/402401/Python-Use-topologically-sorted-items-and-groups-to-get-the-desired-order.
        """

        # Helper function: returns topological order of a graph, if it exists.
        def get_top_order(graph, indegrees):
            top_order = []
            stack = [node for node in range(len(graph)) if indegrees[node] == 0]
            while stack:
                v = stack.pop()
                top_order.append(v)
                for u in graph[v]:
                    indegrees[u] -= 1
                    if indegrees[u] == 0:
                        stack.append(u)
            return top_order if len(top_order) == len(graph) else []

        # STEP 1: Create a new group for each item that belongs to no group.
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        # STEP 2: Build directed graphs for items and groups.
        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m
        for u in range(n):
            for v in beforeItems[u]:
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u] != group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1

        # STEP 3: Find topological orders of items and groups.
        item_order = get_top_order(graph_items, indegree_items)
        group_order = get_top_order(graph_groups, indegree_groups)
        if not item_order or not group_order: return []

        # STEP 4: Find order of items within each group.
        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        # STEP 5. Combine ordered groups.
        res = []
        for group in group_order:
            res += order_within_group[group]
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
          beforeItems=[[], [6], [5], [6], [3, 6], [], [], []]),
     ([6, 3, 4, 1, 5, 2, 0, 7], [7, 0, 5, 2, 6, 3, 4, 1])],
    # [dict(n=8, m=2, group=[-1, -1, 1, 0, 0, 1, 0, -1],
    #       beforeItems=[[], [6], [5], [6], [3], [], [4], []]),
    #  ([],)],
])
def test_solutions(kw, expected):
    assert Solution().sortItems(**kw) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
