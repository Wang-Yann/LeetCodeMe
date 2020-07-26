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
import collections
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

class Solution1:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        使用拓扑排序求解。从所有出度为 0 的单元格开始广度优先搜索，每一轮搜索都会遍历当前层的所有单元格，更新其余单元格的出度，
        并将出度变为 0 的单元格加入下一层搜索。当搜索结束时，搜索的总层数即为矩阵中的最长递增路径的长度。

        """
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        out_degree = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        out_degree[i][j] += 1
                if out_degree[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][column]:
                        out_degree[newRow][newColumn] -= 1
                        if out_degree[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))

        return ans


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
    assert Solution1().longestIncreasingPath(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
