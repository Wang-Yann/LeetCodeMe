#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-06 15:24:09
# @Last Modified : 2020-08-06 15:24:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。 
# 
#  我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。 
# 
#  树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：edges = [[0,1],[0,2]]
# 输出：2
# 解释：
# 这棵树上最长的路径是 1 - 0 - 2，边数为 2。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# 输出：4
# 解释： 
# 这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= edges.length < 10^4 
#  edges[i][0] != edges[i][1] 
#  0 <= edges[i][j] <= edges.length 
#  edges 会形成一棵无向树 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 40 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """挺巧妙的"""
        self.res = 0
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            max1 = max2 = 0
            for neighbor in G[node]:
                if neighbor in visited:
                    continue
                num = dfs(neighbor)
                if num > max1:
                    max1, max2 = num, max1
                elif num > max2:
                    max2 = num
            self.res = max(self.res, max1 + max2)
            return max(max1, max2) + 1

        dfs(0)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        随机选取一个点，返回最远距离的点
        利用最远距离的点作为起始点，再一次DFS，返回距离
        这个才最符合思路
        """
        G = collections.defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        visited = set()
        res = 0
        self.index = 0

        def dfs(node, curlen):
            nonlocal res
            visited.add(node)
            for neighbor in G[node]:
                if neighbor not in visited:
                    res = max(curlen, res)
                    dfs(neighbor, curlen + 1)
            visited.discard(node)
            if curlen > res:
                self.index = node
            return res + 1

        dfs(0, 0)
        # print(res,visited,self.index)
        return dfs(self.index, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(edges=[[0, 1], [0, 2]]), 2],
    [dict(edges=[[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]), 4],
])
def test_solutions(kw, expected):
    assert Solution1().treeDiameter(**kw) == expected
    # assert Solution().treeDiameter(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
