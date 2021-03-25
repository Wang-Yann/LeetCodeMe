#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-01-29 08:20:48
# @Last Modified : 2021-01-29 08:20:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row,
#  col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你
# 每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。 
# 
#  一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。 
# 
#  请你返回从左上角走到右下角的最小 体力消耗值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
# 输出：1
# 解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。
#  
# 
#  示例 3： 
# 
#  
# 输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# 输出：0
# 解释：上图所示路径不需要消耗任何体力。
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == heights.length 
#  columns == heights[i].length 
#  1 <= rows, columns <= 100 
#  1 <= heights[i][j] <= 106 
#  
#  Related Topics 深度优先搜索 并查集 图 二分查找 
#  👍 140 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        dist = [0x7fffffff] * (R * C)
        dist[0] = 0
        seen = set()
        while heap:
            d, x, y = heapq.heappop(heap)
            ident = x * C + y
            if ident in seen:
                continue
            if (x, y) == (R - 1, C - 1):
                break
            seen.add(ident)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= R - 1 and 0 <= ny <= C - 1:
                    nd = max(d, abs(heights[x][y] - heights[nx][ny]))
                    if nd <= dist[nx * C + ny]:
                        dist[nx * C + ny] = nd
                        heapq.heappush(heap, (dist[nx * C + ny], nx, ny))
        return dist[R * C - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]), 2],
    [dict(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]), 1],
    [dict(heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]), 0],
])
def test_solutions(kw, expected):
    assert Solution().minimumEffortPath(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
