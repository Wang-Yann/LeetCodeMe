#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 18:18:50
# @Last Modified : 2020-07-31 18:18:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。 
# 
# 
#  我们为每一位工人分配一辆专属自行车，使每个工人与其分配到的自行车之间的曼哈顿距离最小化。 
# 
#  p1 和 p2 之间的曼哈顿距离为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。 
# 
#  返回每个工人与分配到的自行车之间的曼哈顿距离的最小可能总和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# 输出：6
# 解释：
# 自行车 0 分配给工人 0，自行车 1 分配给工人 1 。分配得到的曼哈顿距离都是 3, 所以输出为 6 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# 输出：4
# 解释：
# 先将自行车 0 分配给工人 0，再将自行车 1 分配给工人 1（或工人 2），自行车 2 给工人 2（或工人 1）。如此分配使得曼哈顿距离的总和为 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000 
#  所有工人和自行车的位置都不相同。 
#  1 <= workers.length <= bikes.length <= 10 
#  
#  Related Topics 动态规划 回溯算法 
#  👍 34 👎 0

"""

import functools
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """GOOD"""
        min_heap = [(0, 0, 0)]
        lookup = set()
        while min_heap:
            cost, i, taken = heapq.heappop(min_heap)
            if (i, taken) in lookup:
                continue
            lookup.add((i, taken))
            if i == len(workers):
                # print(lookup,cost,i,taken)
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j):
                    continue
                heapq.heappush(min_heap, (
                    cost + manhattan(workers[i], bikes[j]),
                    i + 1,
                    taken | (1 << j)
                ))


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """TODO"""
        NW, NB = len(workers), len(bikes)

        @functools.lru_cache(None)
        def dfs(w_idx=0, state=0):
            if w_idx >= NW:
                return 0
            minDis = 0x7fffffff
            for i in range(NB):
                assign = 1 << i
                if state & assign == 0:
                    state |= assign
                    rest = dfs(w_idx + 1, state)
                    state -= assign
                    minDis = min(minDis, rest + manhattan(workers[w_idx], bikes[i]))
            return minDis

        return dfs(0, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]), 6, ],
    [dict(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]), 4]
])
def test_solutions(kw, expected):
    assert Solution().assignBikes(**kw) == expected
    assert Solution1().assignBikes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
