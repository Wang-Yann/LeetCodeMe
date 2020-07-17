#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 20:33:45
# @Last Modified : 2020-04-12 20:33:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
#  示例:
#
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
#  提示：
#
#
#  board 和 word 中只包含大写和小写英文字母。
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#  1 <= word.length <= 10^3
#
#  Related Topics 数组 回溯算法
#  👍 480 👎 0

"""

from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        if not word:
            return True
        m, n = len(board), len(board[0])

        def need_walk_pos(i, j, visited):
            return 0 <= i <= m - 1 and 0 <= j <= n - 1 and (i, j) not in visited

        def existRecu(pos_x, pox_y, curr, visited, k):
            if curr == word:
                return True
            res = False
            for x, y in [
                (pos_x, pox_y - 1), (pos_x, pox_y + 1),
                (pos_x - 1, pox_y), (pos_x + 1, pox_y)]:
                if need_walk_pos(x, y, visited) and board[x][y] == word[k + 1]:
                    visited.append((x, y))
                    res = res or existRecu(x, y, curr + board[x][y], visited, k + 1)
                    visited.pop()

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                if existRecu(i, j, word[0], [(i, j)], 0):
                    return True
        return False

    def existS(self, board, word):
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or \
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result


if __name__ == '__main__':
    sol = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    samples = [
        "ABCCED",
        "SEE",
        "ABCB"
    ]
    res = [sol.exist(board, x) for x in samples]
    print(res)
