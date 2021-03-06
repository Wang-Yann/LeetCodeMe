#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。 
# 
#  移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。 
# 
#  返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释： 
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。 
# 
#  示例 2： 
# 
#  输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 500 
#  1 <= A[i].length <= 500 
#  0 <= A[i][j] <= 1 
#  所有行的大小都相同 
#  
#  Related Topics 深度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        """me 不优雅"""
        R, C = len(A), len(A[0])

        def dfs(i, j):
            if 0 <= i <= R - 1 and 0 <= j <= C - 1 and A[i][j] == 1:
                A[i][j] = 0
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for col in range(C):
            if A[0][col] == 1:
                dfs(0, col)
            if A[R - 1][col] == 1:
                dfs(R - 1, col)
        for row in range(1, R - 1):
            if A[row][0] == 1:
                dfs(row, 0)
            if A[row][C - 1] == 1:
                dfs(row, C - 1)
        return sum(sum(row) for row in A)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]], 3),
    ([[0, 1, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 0]], 0),
])
def test_solutions(args, expected):
    assert Solution().numEnclaves(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
