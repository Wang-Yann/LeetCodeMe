#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。 
# 
#  输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边
# 不属于树中已存在的边。 
# 
#  结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u and v和顶点的边，其中父节点u是子节点v的一个父
# 节点。 
# 
#  返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。 
# 
#  示例 1: 
# 
#  
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
#  
# 
#  示例 2: 
# 
#  
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
#  
# 
#  注意: 
# 
#  
#  二维数组大小的在3到1000范围内。 
#  二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。 
#  
#  Related Topics 树 深度优先搜索 并查集 图

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        并查集
        分为两种情况:
            都是度为1， 则找出构成环的最后一条边
            有度为2的两条边(A->B, C->B)，则删除的边一定是在其中
            先不将C->B加入并查集中，若不能构成环，则C->B是需要删除的点边，反之，则A->B是删除的边(去掉C->B还能构成环，则C->B一定不是要删除的边)

        """
        n = len(edges)
        cand1, cand2 = [], []
        parent = {}
        for st, ed in edges:
            if ed in parent:
                cand1 = [parent[ed], ed]
                cand2 = [st, ed]
            else:
                parent[ed] = st
        uf = UnionFind(n + 1)
        for edge in edges:
            if edge == cand2:
                continue
            if not uf.union_set(*edge):
                return cand1 if cand2 else edge
        return cand2


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [1, 3], [2, 3]], [2, 3]),
    pytest.param([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
])
def test_solutions(args, expected):
    assert Solution().findRedundantDirectedConnection(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
