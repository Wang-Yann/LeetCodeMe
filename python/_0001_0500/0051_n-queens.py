#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  示例: 
# 
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步
# ，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择

    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        ME
        Last %5
        """
        # def format_res_output(res):
        #     output = []
        #     for ans in res:
        #         tmp = []
        #         for pos in ans:
        #             tmp.append("".join(["Q" if x == pos else "." for x in range(n)]))
        #         output.append(tmp)
        #     return output

        res = []

        def is_valid(cur_path, cur_row, cur_col):
            return not any(cur_col == col or
                           abs(cur_row - row) == abs(cur_col - col)
                           for row, col in enumerate(cur_path))
            # for row, col in enumerate(cur_path):
            #     if cur_col == col or abs(cur_row - row) == abs(cur_col - col):
            #         return False
            # return True

        def dfs(cur_row, cur_path):
            if len(cur_path) == n:
                res.append(cur_path[:])
            for i in range(cur_row, n):
                for j in range(n):
                    if is_valid(cur_path, i, j):
                        dfs(i + 1, cur_path + [j])

        dfs(0, [])
        ans = [list(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), ans)) for ans in res]
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """

        # For any point (x,y), if we want the new point (p,q) don't share the same row, column, or diagonal.
        # then there must have ```p+q != x+y``` and ```p-q!= x-y```
        # the former focus on eliminate 'left bottom right top' diagonal
        # the latter focus on eliminate 'left top right bottom' diagonal

        # - col_per_row: the list of column index per row
        # - cur_row：current row we are searching for valid column
        # - xy_diff：the list of x-y
        # - xy_sum：the list of x+y

    """

    def solveNQueens(self, n):
        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row - col not in xy_diff and cur_row + col not in xy_sum:
                    dfs(col_per_row + [col], xy_diff + [cur_row - col], xy_sum + [cur_row + col])

        ress = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in res] for res in ress]


class Solution2:
    """官方"""

    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output


@pytest.mark.parametrize("args,expected", [
    (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    (1, [["Q"]]),
    (2, []),
])
def test_solutions(args, expected):
    assert sorted(Solution().solveNQueens(args)) == sorted(expected)
    assert sorted(Solution1().solveNQueens(args)) == sorted(expected)
    assert sorted(Solution2().solveNQueens(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
