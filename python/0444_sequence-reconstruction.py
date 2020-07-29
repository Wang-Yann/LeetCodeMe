#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 10:20:05
# @Last Modified : 2020-07-29 10:20:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤ 104。重建是指在序列集 
# seqs 中构建最短的公共超序列。（即使得所有 seqs 中的序列都是该最短序列的子序列）。确定是否只可以从 seqs 重建唯一的序列，且该序列就是 org 。
#  
# 
#  示例 1： 
# 
#  输入：
# org: [1,2,3], seqs: [[1,2],[1,3]]
# 
# 输出：
# false
# 
# 解释：
# [1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：
# org: [1,2,3], seqs: [[1,2]]
# 
# 输出：
# false
# 
# 解释：
# 可以重建的序列只有 [1,2]。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
# 
# 输出：
# true
# 
# 解释：
# 序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。
#  
# 
#  
# 
#  示例 4： 
# 
#  输入：
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
# 
# 输出：
# true
#  
#  Related Topics 图 拓扑排序 
#  👍 17 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        拓扑排序
        该题边角条件非常多，很多都是出乎意料的，甚至有悖于常理，需要面面俱到考虑验证。
        首先题目规定结点1～N编号，但给出的边却有超过N的数，
        甚至是负数；
        其次给出的序列可能是空或只有一个点，稍不注意会数组越界；
        再次不同于常规的拓扑排序，比如结点数为1，依赖关系为空，
        则输出序列1也是正确答案，本题要求序列中的点必须在给出的边中出现，故需要额外的记录哪些点在边中出现

        这些边角测试用例出现在87以后,借鉴了下面

        """
        # if not seqs:
        #     return not org
        G = collections.defaultdict(set)
        for seq in seqs:
            for node in seq:
                if node not in G:
                    G[node] = set()
        for seq in seqs:
            for i in range(1, len(seq)):
                G[seq[i - 1]].add(seq[i])
        in_degrees = {u: 0 for u in G}
        for node in G:
            for dst in G[node]:
                in_degrees[dst] += 1
        res = []
        dq = collections.deque([idx for idx, cnt in in_degrees.items() if cnt == 0])
        while dq:
            if len(dq) > 1:
                return False
            u = dq.popleft()
            res.append(u)
            for v in G[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    dq.append(v)
        # print(res)
        if len(G) != len(res):
            return False
        return res == org


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)

        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return None


@pytest.mark.parametrize("kw,expected", [
    [{"org": [1, 2, 3], "seqs": [[1, 2], [1, 3]]}, False],
    [{"org": [1, 2, 3], "seqs": [[1, 2]]}, False],
    [{"org": [1, 2, 3], "seqs": [[1, 2], [1, 3], [2, 3]]}, True],
    [{"org": [4, 1, 5, 2, 6, 3], "seqs": [[5, 2, 6, 3], [4, 1, 5, 2]]}, True],
    [{"org": [1], "seqs": []}, False],
    [{"org": [1], "seqs": [[2]]}, False],
])
def test_solutions(kw, expected):
    assert Solution().sequenceReconstruction(**kw) == expected
    # assert Solution1().sequenceReconstruction(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
