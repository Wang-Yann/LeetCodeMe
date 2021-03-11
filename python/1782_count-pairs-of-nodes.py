#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-11 02:26:14
# @Last Modified : 2021-03-11 02:26:14
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个无向图，无向图由整数 n ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条
# 无向边。同时给你一个代表查询的整数数组 queries 。 
# 
#  第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目： 
# 
#  
#  a < b 
#  cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。 
#  
# 
#  请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答
# 案。 
# 
#  请注意，图中可能会有 重复边 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# 输出：[6,5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries =
#  [1,2,3,4,5]
# 输出：[10,10,9,8,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 2 * 104 
#  1 <= edges.length <= 105 
#  1 <= ui, vi <= n 
#  ui != vi 
#  1 <= queries.length <= 20 
#  0 <= queries[j] < edges.length 
#  
#  Related Topics 图 
#  👍 16 👎 0


import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cnt, res = [0] * (n + 1), [0] * len(queries)
        shared_edges = collections.Counter()
        for n1, n2 in edges:
            cnt[n1] += 1
            cnt[n2] += 1
            shared_edges[(min(n1, n2), max(n1, n2))] += 1
        sorted_node_cnt = sorted(cnt)
        for idx, q in enumerate(queries):
            i, j = 1, n
            while i < j:
                if q < sorted_node_cnt[i] + sorted_node_cnt[j]:
                    res[idx] += j - i
                    j -= 1
                else:
                    i += 1
            for (i, j), sh_cnt in shared_edges.items():
                if cnt[i] + cnt[j] > q >= cnt[i] + cnt[j] - sh_cnt:
                    res[idx] -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3]), [6, 5]],
    [dict(n=5, edges=[[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]], queries=[1, 2, 3, 4, 5]),
     [10, 10, 9, 8, 6]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countPairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
