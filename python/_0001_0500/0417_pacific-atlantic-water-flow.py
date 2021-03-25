#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。 
# 
#  规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。 
# 
#  请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。 
# 
#  
# 
#  提示： 
# 
#  
#  输出坐标的顺序不重要 
#  m 和 n 都小于150 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 给定下面的 5x5 矩阵:
# 
#   太平洋 ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
        DFS
    """

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        PACIFIC, ATLANTIC = 1, 2

        def valid_pos(x, y):
            return 0 <= x <= m - 1 and 0 <= y <= n - 1

        def dfs(x, y, prev_height, prev_label):
            if not valid_pos(x, y) or matrix[x][y] < prev_height \
                    or (visited_labels[x][y] | prev_label) == visited_labels[x][y]:
                return
            visited_labels[x][y] |= prev_label
            if visited_labels[x][y] == (PACIFIC | ATLANTIC):
                res.append([x, y])
            for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(x + direction[0], y + direction[1], matrix[x][y], visited_labels[x][y])

        if not matrix: return []
        res = []
        m, n = len(matrix), len(matrix[0])
        visited_labels = [[0] * n for _ in range(m)]
        for i in range(m):
            dfs(i, 0, float("-inf"), PACIFIC)
            dfs(i, n - 1, float("-inf"), ATLANTIC)
        for j in range(n):
            dfs(0, j, float("-inf"), PACIFIC)
            dfs(m - 1, j, float("-inf"), ATLANTIC)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def __init__(self):
        self.result_all = None
        # 分别表示上右下左
        self.directs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.m = 0
        self.n = 0
        # 表示能流到太平洋
        self.po = None
        # 表示能流到大西洋
        self.ao = None
        self.visited = None

    def pacificAtlantic(self, matrix):
        # 初始化一些东西
        self.result_all = []
        self.m = len(matrix)
        if self.m == 0:
            return self.result_all
        self.n = len(matrix[0])
        self.ao = [[0] * self.n for _ in range(self.m)]
        self.po = [[0] * self.n for _ in range(self.m)]
        self.visited = [[0] * self.n for _ in range(self.m)]

        # 本题顺着流不太好做，我们用逆流的方式来思考
        # 从上面的太平洋逆流
        for i in range(0, 1):
            for j in range(self.n):
                self.dfs(matrix, i, j, True)
        # 从左边的太平洋逆流
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(0, 1):
                self.dfs(matrix, i, j, True)
        # 下面的大西洋
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m - 1, self.m):
            for j in range(self.n):
                self.dfs(matrix, i, j, False)
        # 右边的大西洋
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n - 1, self.n):
                self.dfs(matrix, i, j, False)

        for i in range(self.m):
            for j in range(self.n):
                if self.po[i][j] == 1 and self.ao[i][j] == 1:
                    self.result_all.append([i, j])
        return self.result_all

    def dfs(self, matrix, x, y, flag):
        if self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1
        if flag:
            # 表示是太平洋
            self.po[x][y] = 1
        else:
            # 表示是大西洋
            self.ao[x][y] = 1

        for i in range(4):
            newx = x + self.directs[i][0]
            newy = y + self.directs[i][1]
            if not self.in_area(newx, newy):
                continue
            if matrix[x][y] > matrix[newx][newy]:
                continue
            self.dfs(matrix, newx, newy, flag)
        return

    def in_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]
     ], [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
])
def test_solutions(args, expected):
    assert sorted(Solution().pacificAtlantic(args)) == sorted(expected)
    assert sorted(Solution1().pacificAtlantic(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
