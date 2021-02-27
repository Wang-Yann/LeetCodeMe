#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 13:00:28
# @Last Modified : 2021-02-27 13:00:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。 
# 
#  矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下
# 标从 0 开始计数）执行异或运算得到。 
# 
#  请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 1
# 输出：7
# 解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。 
# 
#  示例 2： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 2
# 输出：5
# 解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。 
# 
#  示例 3： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 3
# 输出：4
# 解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。 
# 
#  示例 4： 
# 
#  输入：matrix = [[5,2],[1,6]], k = 4
# 输出：0
# 解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。 
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 1000 
#  0 <= matrix[i][j] <= 106 
#  1 <= k <= m * n 
#  
#  Related Topics 数组 
#  👍 12 👎 0
  

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """ 最小堆
            GOOD TODO
        """
        R, C = map(len, (matrix, matrix[0]))
        ans = [[0] * (C + 1) for _ in range(R + 1)]
        heap = []
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                ans[r + 1][c + 1] = cell ^ ans[r + 1][c] ^ ans[r][c + 1] ^ ans[r][c]
                heapq.heappush(heap, ans[r + 1][c + 1])
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0]
    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(matrix=[[5, 2], [1, 6]], k=1), 7],
    [dict(matrix=[[5, 2], [1, 6]], k=2), 5],
    [dict(matrix=[[5, 2], [1, 6]], k=3), 4],
    [dict(matrix=[[5, 2], [1, 6]], k=4), 0],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().kthLargestValue(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
