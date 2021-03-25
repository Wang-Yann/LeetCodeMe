#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 
# 
#  
# 
#  示例： 
# 
#  给出如下 3x6 的高度图:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# 
# 返回 4 。
#  
# 
#  
# 
#  如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。 
# 
#  
# 
#  
# 
#  下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 110 
#  0 <= heightMap[i][j] <= 20000 
#  
#  Related Topics 堆 广度优先搜索

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://github.com/grandyang/leetcode/issues/407
    """

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        ans = 0
        heap = []
        visited = set()
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited |= {(0, j), (m - 1, j)}
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited |= {(i, 0), (i, n - 1)}
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while heap:
            height, i, j = heapq.heappop(heap)
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni <= m - 1 and 0 <= nj <= n - 1 and (ni, nj) not in visited:
                    ans += max(0, height - heightMap[ni][nj])
                    heapq.heappush(heap, (max(heightMap[ni][nj], height), ni, nj))
                    visited |= {(ni, nj)}
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [
                [1, 4, 3, 1, 3, 2],
                [3, 2, 1, 3, 2, 4],
                [2, 3, 3, 2, 3, 1]
            ]

            , 4),
])
def test_solutions(args, expected):
    assert Solution().trapRainWater(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
