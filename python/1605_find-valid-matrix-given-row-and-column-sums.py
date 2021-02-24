#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 09:44:36
# @Last Modified : 2021-02-24 09:44:36
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个非负整数数组 rowSum 和 colSum ，其中 rowSum[i] 是二维矩阵中第 i 行元素的和， colSum[j] 是第 j 列元素的和
# 。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。 
# 
#  请找到大小为 rowSum.length x colSum.length 的任意 非负整数 矩阵，且该矩阵满足 rowSum 和 colSum 的要求。 
# 
# 
#  请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个 可行矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：rowSum = [3,8], colSum = [4,7]
# 输出：[[3,0],
#       [1,7]]
# 解释：
# 第 0 行：3 + 0 = 3 == rowSum[0]
# 第 1 行：1 + 7 = 8 == rowSum[1]
# 第 0 列：3 + 1 = 4 == colSum[0]
# 第 1 列：0 + 7 = 7 == colSum[1]
# 行和列的和都满足题目要求，且所有矩阵元素都是非负的。
# 另一个可行的矩阵为：[[1,2],
#                   [3,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：rowSum = [5,7,10], colSum = [8,6,8]
# 输出：[[0,5,0],
#       [6,1,0],
#       [2,0,8]]
#  
# 
#  示例 3： 
# 
#  
# 输入：rowSum = [14,9], colSum = [6,9,8]
# 输出：[[0,9,5],
#       [6,0,3]]
#  
# 
#  示例 4： 
# 
#  
# 输入：rowSum = [1,0], colSum = [1]
# 输出：[[1],
#       [0]]
#  
# 
#  示例 5： 
# 
#  
# 输入：rowSum = [0], colSum = [0]
# 输出：[[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rowSum.length, colSum.length <= 500 
#  0 <= rowSum[i], colSum[i] <= 108 
#  sum(rows) == sum(columns) 
#  
#  Related Topics 贪心算法 
#  👍 17 👎 0

"""
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        i行j列设为　min(row[i], col[j])，同时更新row[i] 和col[j]即可

        """
        row, col = rowSum, colSum
        m, n = len(row), len(col)
        A = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                A[i][j] = min(row[i], col[j])
                row[i] -= A[i][j]
                col[j] -= A[i][j]
        return A


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(rowSum=[3, 8], colSum=[4, 7]), [[3, 0], [1, 7]]],
    [dict(rowSum=[5, 7, 10], colSum=[8, 6, 8]), [[0, 5, 0], [6, 1, 0], [2, 0, 8]]],
    [dict(rowSum=[14, 9], colSum=[6, 9, 8]), [[0, 9, 5], [6, 0, 3]]],
    [dict(rowSum=[1, 0], colSum=[1]), [[1], [0]]],
    [dict(rowSum=[0], colSum=[0]), [[0]]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    resMatrix = SolutionCLS().restoreMatrix(**copy.deepcopy(kw))

    rows = list(map(sum, resMatrix))
    cols = list(map(sum, zip(*resMatrix)))
    assert kw["rowSum"] == rows
    assert kw["colSum"] == cols


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
