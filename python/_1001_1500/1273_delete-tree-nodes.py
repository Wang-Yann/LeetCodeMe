#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 13:46:00
# @Last Modified : 2020-08-07 13:46:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵以节点 0 为根节点的树，定义如下： 
# 
#  
#  节点的总数为 nodes 个； 
#  第 i 个节点的值为 value[i] ； 
#  第 i 个节点的父节点是 parent[i] 。 
#  
# 
#  请你删除节点值之和为 0 的每一棵子树。 
# 
#  在完成所有删除之后，返回树中剩余节点的数目。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nodes <= 10^4 
#  -10^5 <= value[i] <= 10^5 
#  parent.length == nodes 
#  parent[0] == -1 表示节点 0 是树的根。 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 12 👎 0

"""

import collections
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        G = collections.defaultdict(list)
        for idx, p in enumerate(parent):
            if p != -1:
                G[p].append(idx)
        node_cnt = [1] * nodes

        def dfs(node):
            for child in G[node]:
                dfs(child)
                value[node] += value[child]
                node_cnt[node] += node_cnt[child]
            if value[node] == 0:
                node_cnt[node] = 0

        dfs(0)
        # print(node_cnt)
        return node_cnt[0]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        """拓扑排序"""
        in_deg = [0] * nodes
        for p in parent:
            if p != -1:
                in_deg[p] += 1

        node_cnt = [1] * nodes
        dq = collections.deque([i for i in range(nodes) if in_deg[i] == 0])

        while dq:
            node = dq.popleft()
            if value[node] == 0:
                node_cnt[node] = 0
            p = parent[node]
            if p != -1:
                value[p] += value[node]
                node_cnt[p] += node_cnt[node]
                in_deg[p] -= 1
                if in_deg[p] == 0:
                    dq.append(p)
        # print(node_cnt)
        return node_cnt[0]


@pytest.mark.parametrize("kw,expected", [
    [dict(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -1]), 2],
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    assert Solution().deleteTreeNodes(**kw) == expected
    assert Solution1().deleteTreeNodes(**kw1) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
