#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 10:23:48
# @Last Modified : 2021-02-23 10:23:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个无向图，整数 n 表示图中节点的数目，edges 数组表示图中的边，其中 edges[i] = [ui, vi] ，表示 ui 和 vi 之间有一条
# 无向边。 
# 
#  一个 连通三元组 指的是 三个 节点组成的集合且这三个点之间 两两 有边。 
# 
#  连通三元组的度数 是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。 
# 
#  请你返回所有连通三元组中度数的 最小值 ，如果图中没有连通三元组，那么返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# 输出：3
# 解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# 输出：0
# 解释：有 3 个三元组：
# 1) [1,4,3]，度数为 0 。
# 2) [2,5,6]，度数为 2 。
# 3) [5,6,7]，度数为 2 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 400 
#  edges[i].length == 2 
#  1 <= edges.length <= n * (n-1) / 2 
#  1 <= ui, vi <= n 
#  ui != vi 
#  图中没有重复的边。 
#  
#  Related Topics 图 
#  👍 9 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        """
        GOOD
        https://leetcode-cn.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/solution/xiang-fa-bu-yong-duo-bao-li-yi-ba-suo-by-3mds/
        """
        indegrees = collections.defaultdict(lambda: set())
        res = float("inf")
        for u, v in edges:
            indegrees[u].add(v)
            indegrees[v].add(u)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if j in indegrees[i] and k in indegrees[i] and k in indegrees[j]:
                        d = len(indegrees[i]) + len(indegrees[j]) + len(indegrees[k]) - 6
                        res = min(res, d)
        return res if res != float("inf") else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=6, edges=[[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]), 3],
    [dict(n=7, edges=[[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]), 0],
])
def test_solutions(kw, expected):
    assert Solution().minTrioDegree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
