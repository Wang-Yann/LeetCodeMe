#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 18:04:58
# @Last Modified : 2020-07-31 18:04:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。 
# 
# 
#  我们需要为每位工人分配一辆自行车。在所有可用的自行车和工人中，我们选取彼此之间曼哈顿距离最短的工人自行车对 (worker, bike) ，并将其中的自行
# 车分配給工人。如果有多个 (worker, bike) 对之间的曼哈顿距离相同，那么我们选择工人索引最小的那对。类似地，如果有多种不同的分配方法，则选择自行车索
# 引最小的一对。不断重复这一过程，直到所有工人都分配到自行车为止。 
# 
#  给定两点 p1 和 p2 之间的曼哈顿距离为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。 
# 
#  返回长度为 n 的向量 ans，其中 a[i] 是第 i 位工人分配到的自行车的索引（从 0 开始）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
# 输出：[1,0]
# 解释：
# 工人 1 分配到自行车 0，因为他们最接近且不存在冲突，工人 0 分配到自行车 1 。所以输出是 [1,0]。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
# 输出：[0,2,1]
# 解释：
# 工人 0 首先分配到自行车 0 。工人 1 和工人 2 与自行车 2 距离相同，因此工人 1 分配到自行车 2，工人 2 将分配到自行车 1 。因此输出为 
# [0,2,1]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= workers[i][j], bikes[i][j] < 1000 
#  所有工人和自行车的位置都不相同。 
#  1 <= workers.length <= bikes.length <= 1000 
#  
#  Related Topics 贪心算法 排序 
#  👍 32 👎 0

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def assignBikes(self, workers, bikes):
        """GOOD"""

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        NW = len(workers)
        NB = len(bikes)
        distances = [[] for _ in range(NW)]
        for i in range(NW):
            for j in range(NB):
                distances[i].append((manhattan(workers[i], bikes[j]), i, j))
            distances[i].sort(reverse=True)

        result = [None] * NW
        lookup = set()
        min_heap = []
        for i in range(NW):
            heapq.heappush(min_heap, distances[i].pop())
        # """GOOD"""
        while len(lookup) < NW:
            _, worker, bike = heapq.heappop(min_heap)
            if bike not in lookup:
                result[worker] = bike
                lookup.add(bike)
            else:
                heapq.heappush(min_heap, distances[worker].pop())
        return result


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        TODO 1000*1000　内存没爆掉吗
        将所有的自行车和工人两两配对，求出距离后 按距离存到桶里
        如果我们工人和自行车配对时候，先按工人从小到大枚举，再按自行车编号从小到大
        那么先进桶的配对方案满足下面的三关键字排序
        第一关键字是距离大小
        第二关键字是工人编号
        第三关键字是自行车编号
        排序完成后遍历桶排序数组，如果扫到的工人和自行车都还没分配，就把当前的自行车分配给当前工人，否则就继续扫下一个

        """
        # 工人和车子数量
        NW = len(workers)
        NB = len(bikes)
        # 排序数组，存放距离 工人编号 车子编号
        sol = [0 for i in range(NW * NB)]
        for i in range(NW):
            for j in range(NB):
                # 计算距离
                cost = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                # 压入sol
                sol[i * NB + j] = [cost, i, j]

        # 对按照距离 工人编号 车子编号 三关键字排序
        sol.sort()

        # 标记工人有没有分配车子
        visisted_worker = [False] * NW
        # 标记车子有没有被分配
        visisted_bike = [False] * NB

        # 答案数组
        ans = [0 for i in range(NW)]
        for i in range(len(sol)):
            # 人和车的编号
            cost, workersIdx, bikeIdx = sol[i]
            # 车和人都还没有分配
            if visisted_worker[workersIdx] == False and visisted_bike[bikeIdx] == False:
                visisted_worker[workersIdx] = visisted_bike[bikeIdx] = True
                ans[workersIdx] = bikeIdx
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]), [1, 0]],
    [dict(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]), [0, 2, 1]],
])
def test_solutions(kw, expected):
    assert Solution().assignBikes(**kw) == expected
    assert Solution1().assignBikes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
