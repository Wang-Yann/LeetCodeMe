#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。 
# 
#  现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 更具体地说, 存在一个自然数 K, 无论选择从哪里开始行走, 我们走了不到 K 步后必能
# 停止在一个终点。 
# 
#  哪些节点最终是安全的？ 结果返回一个有序的数组。 
# 
#  该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数. 图以以下的形式给出: graph[i] 是节点 j 
# 的一个列表，满足 (i, j) 是图的一条有向边。 
# 
#  
# 示例：
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 这里是上图的示意图。
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  graph 节点数不超过 10000. 
#  图的边数不会超过 32000. 
#  每个 graph[i] 被排序为不同的整数列表， 在区间 [0, graph.length - 1] 中选取。 
#  
#  Related Topics 深度优先搜索 图

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):

    def eventualSafeNodes(self, graph):
        """
        TODO TODO
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return list(filter(dfs, range(len(graph))))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        拓扑排序
        """
        length = len(graph)
        safe = [False] * length
        graph = list(map(set, graph))
        reverse_graph = [set() for _ in range(length)]
        q = collections.deque()
        for idx, js in enumerate(graph):
            if not js:
                q.append(idx)
            for j in js:
                reverse_graph[j].add(idx)
        while q:
            j = q.popleft()
            safe[j] = True
            for i in reverse_graph[j]:
                graph[i].remove(j)
                if not graph[i]:
                    q.append(i)
        return [i for i, v in enumerate(safe) if v]


@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
])
def test_solutions(args, expected):
    assert Solution().eventualSafeNodes(args) == expected
    assert Solution1().eventualSafeNodes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
