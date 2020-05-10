#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数矩阵，找出最长递增路径的长度。 
# 
#  对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。 
# 
#  示例 1: 
# 
#  输入: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。 
# 
#  示例 2: 
# 
#  输入: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#  
#  Related Topics 深度优先搜索 拓扑排序 记忆化

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """DFS + Memoization Solution
        记忆化的方案1..2..
        """

        @functools.lru_cache(None)
        def get_longestpath(i, j):
            # if max_lengths[i][j]:
            #     return max_lengths[i][j]
            max_depth = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, get_longestpath(x, y))
            # max_lengths[i][j] = max_depth + 1
            # return max_lengths[i][j]
            return max_depth + 1

        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        # max_lengths = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(get_longestpath(i, j), res)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1]
            ]
            , 4),
    pytest.param(
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ],
        4),
])
def test_solutions(args, expected):
    assert Solution().longestIncreasingPath(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
