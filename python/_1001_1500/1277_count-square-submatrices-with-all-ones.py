#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix =
# [
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
# ]
# 输出：15
# 解释： 
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
#  
# 
#  示例 2： 
# 
#  输入：matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。 
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 300 
#  1 <= arr[0].length <= 300 
#  0 <= arr[i][j] <= 1 
#  
#  Related Topics 数组 动态规划

"""

from typing import List
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        TODO
        https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        # print(dp,sep="\n")
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([
         [0, 1, 1, 1],
         [1, 1, 1, 1],
         [0, 1, 1, 1]
     ], 15),
    ([
         [1, 0, 1],
         [1, 1, 0],
         [1, 1, 0]
     ], 7)
])
def test_solutions(args, expected):
    assert Solution().countSquares(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
