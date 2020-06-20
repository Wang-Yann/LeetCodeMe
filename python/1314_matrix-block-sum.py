#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 ma
# t[r][c] 的和： 
# 
#  
#  i - K <= r <= i + K, j - K <= c <= j + K 
#  (r, c) 在矩阵内。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#  
# 
#  示例 2： 
# 
#  输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n, K <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
        二维前缀和
        我们用数组 P 表示数组 mat 的二维前缀和，P 的维数为 (m + 1) * (n + 1)，其中 P[i][j] 表示数组 mat 中以 (0, 0) 为左上角，
        (i - 1, j - 1) 为右下角的矩形子数组的元素之和。
        题目需要对数组 mat 中的每个位置，计算以 (i - K, j - K) 为左上角，(i + K, j + K) 为右下角的矩形子数组的元素之和，我们可以在前缀和数组的帮助下，通过：
            sum = P[i + K + 1][j + K + 1] - P[i - K][j + K + 1] - P[i + K + 1][j - K] + P[i - K][j - K]
        """
        m, n = len(mat), len(mat[0])
        P = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                P[i + 1][j + 1] = P[i + 1][j] + P[i][j + 1] - P[i][j] + mat[i][j]
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(i - K, 0), max(j - K, 0), min(i + K + 1, m), min(j + K + 1, n)
                result[i][j] = P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]
        return result


# leetcode submit region end(Prohibit modification and deletion)



@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1
    ), [[12, 21, 16], [27, 45, 33], [24, 39, 28]]),
    pytest.param(dict(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=2), [[45, 45, 45], [45, 45, 45], [45, 45, 45]]),
])
def test_solutions(kwargs, expected):
    assert Solution().matrixBlockSum(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
