#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-01-27 22:49:40
# @Last Modified : 2021-01-27 22:49:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边： 
# 
#  
#  类型 1：只能由 Alice 遍历。 
#  类型 2：只能由 Bob 遍历。 
#  类型 3：Alice 和 Bob 都可以遍历。 
#  
# 
#  给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请
# 你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图
# 是可以完全遍历的。 
# 
#  返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# 输出：2
# 解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所
# 以可以删除的最大边数是 2 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# 输出：0
# 解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# 输出：-1
# 解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2) 
#  edges[i].length == 3 
#  1 <= edges[i][0] <= 3 
#  1 <= edges[i][1] < edges[i][2] <= n 
#  所有元组 (typei, ui, vi) 互不相同 
#  
#  Related Topics 并查集 
#  👍 95 👎 0
  

"""

import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)

class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))
        self.size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.size -= 1
        return True


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0

        # 节点编号改为从 0 开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not ufa.union_set(u, v):
                    ans += 1
                else:
                    ufb.union_set(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                # Alice 独占边
                if not ufa.union_set(u, v):
                    ans += 1
            elif t == 2:
                # Bob 独占边
                if not ufb.union_set(u, v):
                    ans += 1

        if ufa.size != 1 or ufb.size != 1:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]), 2],
    pytest.param(dict(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]), 0),
    pytest.param(dict(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]), -1),
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution
])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().maxNumEdgesToRemove(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
