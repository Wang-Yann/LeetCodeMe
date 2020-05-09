#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        BFS

        """
        if not board:
            return
        m, n = len(board), len(board[0])
        q = collections.deque()
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "V"
                q.append((i, 0))
            if board[i][n - 1] == "O":
                board[i][n - 1] = "V"
                q.append((i, n - 1))
        for j in range(1, n - 1):
            if board[0][j] == "O":
                board[0][j] = "V"
                q.append((0, j))
            if board[m - 1][j] == "O":
                board[m - 1][j] = "V"
                q.append((m - 1, j))
        while q:
            i, j = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and board[x][y] == "O":
                    board[x][y] = "V"
                    q.append((x, y))
        for i in range(m):
            for j in range(n):
                if board[i][j] != "V":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"


# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    assert board == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
