#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 06:16:03
# @Last Modified : 2021-02-23 06:16:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表示点 ui 和点 vi 之间有一条
# 长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。 
# 
#  给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每个查询 queries[j] ，判断
# 是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严格小于 limitj 。 
# 
#  请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当 queries[j] 的查询结果为 t
# rue 时， answer 第 j 个值为 true ，否则为 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0
# ,2,5]]
# 输出：[false,true]
# 解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
# 对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
# 对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],
# [1,4,13]]
# 输出：[true,false]
# 解释：上图为给定数据。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 105 
#  1 <= edgeList.length, queries.length <= 105 
#  edgeList[i].length == 3 
#  queries[j].length == 3 
#  0 <= ui, vi, pj, qj <= n - 1 
#  ui != vi 
#  pj != qj 
#  1 <= disi, limitj <= 109 
#  两个点之间可能有 多条 边。 
#  
#  Related Topics 排序 并查集 
#  👍 34 👎 0

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        离线算法/在线算法
        """
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edges_list = sorted((w, u, v) for u, v, w in edgeList)

        ans = [True] * len(queries)
        ii = 0
        uf = UnionFind(n)
        for w, p, q, i in queries:
            while ii < len(edges_list) and edges_list[ii][0] < w:
                _, u, v = edges_list[ii]
                uf.union_set(u, v)
                ii += 1
            ans[i] = uf.find_set(p) == uf.find_set(q)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], queries=[[0, 1, 2], [0, 2, 5]]), [False, True]],
    [dict(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], queries=[[0, 4, 14], [1, 4, 13]]),
     [True, False]],
])
def test_solutions(kw, expected):
    assert Solution().distanceLimitedPathsExist(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
