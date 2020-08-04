#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 16:35:08
# @Last Modified : 2020-08-04 16:35:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 R 行 C 列的整数矩阵 A。矩阵上的路径从 [0,0] 开始，在 [R-1,C-1] 结束。 
# 
#  路径沿四个基本方向（上、下、左、右）展开，从一个已访问单元格移动到任一相邻的未访问单元格。 
# 
#  路径的得分是该路径上的 最小 值。例如，路径 8 → 4 → 5 → 9 的值为 4 。 
# 
#  找出所有路径中得分 最高 的那条路径，返回其 得分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[5,4,5],[1,2,6],[7,4,6]]
# 输出：4
# 解释： 
# 得分最高的路径用黄色突出显示。 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[[2,2,1,2,2,2],[1,2,2,2,1,2]]
# 输出：2 
# 
#  示例 3： 
# 
#  
# 
#  输入：[[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
# 输出：3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= R, C <= 100 
#  0 <= A[i][j] <= 10^9 
#  
#  Related Topics 深度优先搜索 并查集 图 
#  👍 35 👎 0

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        """Dijkstra"""
        R, C = len(A), len(A[0])
        max_heap = [(-A[0][0], 0, 0)]
        seen = {(0, 0)}
        while max_heap:
            d, r, c = heapq.heappop(max_heap)
            if r == R - 1 and c == C - 1:
                return -d
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(max_heap, (-min(-d, A[nr][nc]), nr, nc))
        return -1



# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[5, 4, 5],
      [1, 2, 6],
      [7, 4, 6]], 4),
    ([[2, 2, 1, 2, 2, 2],
      [1, 2, 2, 2, 1, 2]], 2),
    ([[3, 4, 6, 3, 4],
      [0, 2, 1, 1, 7],
      [8, 8, 3, 2, 7],
      [3, 2, 4, 9, 8],
      [4, 1, 2, 0, 0],
      [4, 6, 5, 4, 3]], 3),
    ([[0, 1, 0, 0, 0, 1],
      [0, 1, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 1],
      [0, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1]], 0),
])
def test_solutions(args, expected):
    assert Solution().maximumMinimumPath(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
