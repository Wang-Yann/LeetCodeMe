#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法

"""
import collections
import copy
import string
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        https://leetcode-cn.com/problems/sudoku-solver/solution/pythonsethui-su-chao-guo-95-by-mai-mai-mai-mai-zi/
        """
        N = len(board)
        row = [set(range(1, N + 1)) for _ in range(N)]  # 行剩余可用数字
        col = [set(range(1, N + 1)) for _ in range(N)]  # 列剩余可用数字
        block = [set(range(1, N + 1)) for _ in range(N)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    row[i].discard(val)
                    col[j].discard(val)
                    idx_block = (i // 3) * 3 + j // 3
                    block[idx_block].discard(val)
                else:
                    empty.append((i, j))

        def backtrack(idx=0):
            if idx == len(empty):
                return True
            i, j = empty[idx]
            b = (i // 3) * 3 + j // 3
            for v in row[i] & col[j] & block[b]:
                # print(i,j,v,row[i]&col[j]&block[b])
                row[i].discard(v)
                col[j].discard(v)
                block[b].discard(v)
                board[i][j] = str(v)
                if backtrack(idx + 1):
                    return True
                row[i].add(v)
                col[j].add(v)
                block[b].add(v)
            return False

        backtrack(0)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def solveSudoku(self, board: List[List[str]]) -> None:
        N = len(board)
        self.sudoku_solved = False
        # init rows, columns and boxes

        box_index = lambda row, col: (row // 3) * 3 + col // 3

        def could_place(d, row, col):
            if d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)]:
                return False
            return True

        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            rows[row].pop(d)
            columns[col].pop(d)
            boxes[box_index(row, col)].pop(d)
            board[row][col] = '.'

        def place_next_number(row, col):
            if row == col == N - 1:
                self.sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for d in range(1, N + 1):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if not self.sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)

        rows = [collections.defaultdict(int) for _ in range(N)]
        columns = [collections.defaultdict(int) for _ in range(N)]
        boxes = [collections.defaultdict(int) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    d = int(board[i][j])
                    place_number(d, i, j)
        backtrack(0, 0)


class Solution2:

    def solveSudoku(self, board: List[List[str]]) -> None:
        N = len(board)

        def is_valid(i, j, val):
            for x in range(N):
                if board[x][j] == val:
                    return False
            for y in range(N):
                if board[i][y] == val:
                    return False
            row, col = i - i % 3, j - j % 3
            for x in range(3):
                for y in range(3):
                    if board[x + row][y + col] == val:
                        return False
            return True

        def helper(i, j):
            if i >= 9:
                return True
            if j >= 9:
                return helper(i + 1, 0)
            if board[i][j] != ".":
                return helper(i, j + 1)
            for char in string.digits[1:]:
                if not is_valid(i, j, char):
                    continue
                board[i][j] = char
                if helper(i, j + 1):
                    return True
                board[i][j] = "."
            return False

        helper(0, 0)


@pytest.mark.parametrize("board,expected", [
    ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
      ["6", ".", ".", "1", "9", "5", ".", ".", "."],
      [".", "9", "8", ".", ".", ".", ".", "6", "."],
      ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
      ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
      [".", "6", ".", ".", ".", ".", "2", "8", "."],
      [".", ".", ".", "4", "1", "9", ".", ".", "5"],
      [".", ".", ".", ".", "8", ".", ".", "7", "9"]],

     [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
      ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
      ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
      ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
      ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
      ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
      ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
      ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
      ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2])
def test_solutions(board, expected, SolutionCLS):
    board0 = copy.deepcopy(board)
    SolutionCLS().solveSudoku(board0)
    assert board0 == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
