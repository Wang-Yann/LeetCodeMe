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
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
# 
#  示例: 
# 
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
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

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def totalNQueens(self, n: int) -> int:
        """
        Me
        """
        ans = 0

        def is_valid(cur_path, cur_row, cur_col):
            for row, col in enumerate(cur_path):
                if cur_col == col or abs(cur_row - row) == abs(cur_col - col):
                    return False
            return True

        def dfs(cur_row, cur_path):
            nonlocal ans
            if len(cur_path) == n:
                ans += 1
            for i in range(cur_row, n):
                for j in range(n):
                    if is_valid(cur_path, i, j):
                        dfs(i + 1, cur_path + [j])

        dfs(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)


class Solution2:
    """
    x & (−x) 可以获得 xx 的二进制表示中的最低位的 1 的位置；
    x & (x−1) 可以将 xx 的二进制表示中的最低位的 1 置成 0。
    每次获得可以放置皇后的位置中的最低位，并将该位的值置成 0
    ，尝试在该位置放置皇后。这样即可遍历每个可以放置皇后的位置
    """

    def totalNQueens(self, n: int) -> int:
        def solve(row: int, columns: int, diagonals1: int, diagonals2: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    count += solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)
                return count

        return solve(0, 0, 0, 0)


@pytest.mark.parametrize("args,expected", [
    (4, 2),
    (1, 1),
    (2, 0),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().totalNQueens(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
