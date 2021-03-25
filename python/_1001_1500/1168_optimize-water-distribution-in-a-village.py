#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 14:19:04
# @Last Modified : 2020-08-05 14:19:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。 
# 
#  对于每个房子 i，我们有两种可选的供水方案： 
# 
#  
#  一种是直接在房子内建造水井，成本为 wells[i]； 
#  另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，其中每个 pipes[i] = [house1, house2, cost
# ] 代表用管道将 house1 和 house2 连接在一起的成本。当然，连接是双向的。 
#  
# 
#  请你帮忙计算为所有房子都供水的最低总成本。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# 输出：3
# 解释： 
# 上图展示了铺设管道连接房屋的成本。
# 最好的策略是在第一个房子里建造水井（成本为 1），然后将其他房子铺设管道连起来（成本为 2），所以总成本为 3。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10000 
#  wells.length == n 
#  0 <= wells[i] <= 10^5 
#  1 <= pipes.length <= 10000 
#  1 <= pipes[i][0], pipes[i][1] <= n 
#  0 <= pipes[i][2] <= 10^5 
#  pipes[i][0] != pipes[i][1] 
#  
#  Related Topics 并查集 图 
#  👍 25 👎 0

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        self.size -= 1
        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        """
        TODO
        最小生成树 kruskal算法
        因为只修建管道是没有水的，所以必须在至少一个房子内直接建水井。我们可以假设有一个水库，
        水库到每一个房子的成本就是房子内建造水井的成本，这样我们就把本题变成了最基础的最小生成树的问题。假设水库的 id 为 0
        """
        w = [(c, 0, i) for i, c in enumerate(wells, 1)]
        p = [(c, i, j) for i, j, c in pipes]
        res = 0
        uf = UnionFind(n + 1)
        for c, x, y in sorted(w + p):
            if uf.union_set(x, y):
                res += c
            if uf.size == 1:
                break
        return res


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    """
    Prim算法 ;比上面慢很多
    """

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        G = collections.defaultdict(list)
        for i, cost in enumerate(wells, 1):
            G[0].append((i, cost))
            G[i].append((0, cost))
        for a, b, cost in pipes:
            G[a].append((b, cost))
            G[b].append((a, cost))
        seen = set()
        out_edges = [(0, 0)]
        ans = 0
        while out_edges:
            cost, node = heapq.heappop(out_edges)
            if node not in seen:
                seen.add(node)
                ans += cost
                for next_node, next_cost in G[node]:
                    heapq.heappush(out_edges, (next_cost, next_node))
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]), 3],
])
def test_solutions(kw, expected):
    assert Solution().minCostToSupplyWater(**kw) == expected
    assert Solution1().minCostToSupplyWater(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
