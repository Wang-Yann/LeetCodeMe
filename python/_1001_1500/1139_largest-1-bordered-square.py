#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,1,0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 100 
#  1 <= grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/problems/largest-1-bordered-square/solution/qian-zhui-he-python3-by-smoon1989/
        """
        # 矩阵规模
        M, N, sum_val = len(grid), len(grid[0]), 0
        # 四个方向上的前缀和
        L = [[0] * (N + 1) for _ in range(M + 1)]
        U = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                # 矩阵和
                sum_val += grid[i][j]
                # L[i][j] 表示 (i, j) 的左边有多少个 1
                L[i][j + 1] = L[i][j] + grid[i][j]
                # U[i][j] 表示 (i, j) 的上边有多少个 1
                U[i + 1][j] = U[i][j] + grid[i][j]
        # print(L)
        # print(U)
        if sum_val == 0:
            return 0
        # 四条边上 1 的个数
        edges = [0, 0, 0, 0]
        for e in range(min(M, N), 0, -1):
            for i in range(M - e + 1):
                for j in range(N - e + 1):
                    # 判断上边
                    edges[0] = L[i][j + e] - L[i][j]
                    # 判断下边
                    edges[1] = L[i + e - 1][j + e] - L[i + e - 1][j]
                    # 判断左边
                    edges[2] = U[i + e][j] - U[i][j]
                    # 判断右边
                    edges[3] = U[i + e][j + e - 1] - U[i][j + e - 1]
                    # 判断是否满足
                    if all([edge == e for edge in edges]):
                        return e * e
        return 0


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]], 9),
    # ([[1, 1, 0, 0]], 1),
])
def test_solutions(args, expected):
    assert Solution().largest1BorderedSquare(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
