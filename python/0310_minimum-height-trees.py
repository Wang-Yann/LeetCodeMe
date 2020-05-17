#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函
# 数找到所有的最小高度树并返回他们的根节点。 
# 
#  格式 
# 
#  该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。 
# 
#  你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。 
# 
#  示例 1: 
# 
#  输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
#         0
#         |
#         1
#        / \
#       2   3 
# 
# 输出: [1]
#  
# 
#  示例 2: 
# 
#  输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 
# 
# 输出: [3, 4] 
# 
#  说明: 
# 
#  
#  根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。 
#  树的高度是指根节点和叶子节点之间最长向下路径上边的数量。 
#  
#  Related Topics 广度优先搜索 图

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        用拓扑排序即可
首先我们将所有的叶子节点都放入队列中
之后每次有点从队列中出来，就将和这个点相邻的没有入队过的点加入到队列中
容易想到，答案的数量最多不超过两个，所以只要比较最后两个出队的点即可
https://www.jiuzhang.com/solution/minimum-height-trees#tag-highlight-lang-python
        """
        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # the intuition is that in a connected graph,
        # if you pick a node of degree 1 as the root
        # then the resulting tree has the max ht.
        # so trim the leaves until there are at most 2
        # and at least 1 node left.
        leaves = [x for x in range(n) if len(graph[x]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].discard(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=4, edges=[[1, 0], [1, 2], [1, 3]]), [1]),
    pytest.param(dict(n=6, edges=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]), [3, 4]),
])
def test_solutions(kwargs, expected):
    assert Solution().findMinHeightTrees(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
