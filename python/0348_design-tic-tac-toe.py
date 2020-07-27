#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 17:42:16
# @Last Modified : 2020-07-27 17:42:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请在 n × n 的棋盘上，实现一个判定井字棋（Tic-Tac-Toe）胜负的神器，判断每一次玩家落子后，是否有胜出的玩家。 
# 
#  在这个井字棋游戏中，会有 2 名玩家，他们将轮流在棋盘上放置自己的棋子。 
# 
#  在实现这个判定器的过程中，你可以假设以下这些规则一定成立： 
# 
#  1. 每一步棋都是在棋盘内的，并且只能被放置在一个空的格子里； 
# 
#  2. 一旦游戏中有一名玩家胜出的话，游戏将不能再继续； 
# 
#  3. 一个玩家如果在同一行、同一列或者同一斜对角线上都放置了自己的棋子，那么他便获得胜利。 
# 
#  示例: 
# 
#  给定棋盘边长 n = 3, 玩家 1 的棋子符号是 "X"，玩家 2 的棋子符号是 "O"。
# 
# TicTacToe toe = new TicTacToe(3);
# 
# toe.move(0, 0, 1); -> 函数返回 0 (此时，暂时没有玩家赢得这场对决)
# |X| | |
# | | | |    // 玩家 1 在 (0, 0) 落子。
# | | | |
# 
# toe.move(0, 2, 2); -> 函数返回 0 (暂时没有玩家赢得本场比赛)
# |X| |O|
# | | | |    // 玩家 2 在 (0, 2) 落子。
# | | | |
# 
# toe.move(2, 2, 1); -> 函数返回 0 (暂时没有玩家赢得比赛)
# |X| |O|
# | | | |    // 玩家 1 在 (2, 2) 落子。
# | | |X|
# 
# toe.move(1, 1, 2); -> 函数返回 0 (暂没有玩家赢得比赛)
# |X| |O|
# | |O| |    // 玩家 2 在 (1, 1) 落子。
# | | |X|
# 
# toe.move(2, 0, 1); -> 函数返回 0 (暂无玩家赢得比赛)
# |X| |O|
# | |O| |    // 玩家 1 在 (2, 0) 落子。
# |X| |X|
# 
# toe.move(1, 0, 2); -> 函数返回 0 (没有玩家赢得比赛)
# |X| |O|
# |O|O| |    // 玩家 2 在 (1, 0) 落子.
# |X| |X|
# 
# toe.move(2, 1, 1); -> 函数返回 1 (此时，玩家 1 赢得了该场比赛)
# |X| |O|
# |O|O| |    // 玩家 1 在 (2, 1) 落子。
# |X|X|X|
#  
# 
#  
# 
#  进阶: 
# 您有没有可能将每一步的 move() 操作优化到比 O(n2) 更快吗? 
#  Related Topics 设计 
#  👍 26 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class TicTacToe:
    """
    TODO
    巧妙
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.Rsum = [[0] * n, [0] * n]
        self.Csum = [[0] * n, [0] * n]

        self.DIAGONAL = [0, 0]
        self.ANTI_DIAGONAL = [0, 0]

        self.l = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param i The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        i = player - 1

        self.Rsum[i][row] += 1
        self.Csum[i][col] += 1
        if row == col:
            self.DIAGONAL[i] += 1
        if row + col == self.l - 1:
            self.ANTI_DIAGONAL[i] += 1

        if self.Rsum[i][row] == self.l \
                or self.Csum[i][col] == self.l \
                or self.DIAGONAL[i] == self.l \
                or self.ANTI_DIAGONAL[i] == self.l:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    toe = TicTacToe(3)
    assert toe.move(0, 0, 1) == 0  # -> 函数返回 0 (此时，暂时没有玩家赢得这场对决)
    # |X| | |
    # | | | |    // 玩家 1 在 (0, 0) 落子。
    # | | | |
    #
    assert toe.move(0, 2, 2) == 0  # 函数返回 0 (暂时没有玩家赢得本场比赛)
    # |X| |O|
    # | | | |    // 玩家 2 在 (0, 2) 落子。
    # | | | |
    #
    assert toe.move(2, 2, 1) == 0  # ; -> 函数返回 0 (暂时没有玩家赢得比赛)
    # |X| |O|
    # | | | |    // 玩家 1 在 (2, 2) 落子。
    # | | |X|
    #
    assert toe.move(1, 1, 2) == 0  # ; -> 函数返回 0 (暂没有玩家赢得比赛)
    # |X| |O|
    # | |O| |    // 玩家 2 在 (1, 1) 落子。
    # | | |X|
    #
    assert toe.move(2, 0, 1) == 0  # ; -> 函数返回 0 (暂无玩家赢得比赛)
    # |X| |O|
    # | |O| |    // 玩家 1 在 (2, 0) 落子。
    # |X| |X|
    #
    assert toe.move(1, 0, 2) == 0  # ; -> 函数返回 0 (没有玩家赢得比赛)
    # |X| |O|
    # |O|O| |    // 玩家 2 在 (1, 0) 落子.
    # |X| |X|
    #
    assert toe.move(2, 1, 1) == 1  # ; -> 函数返回 1 (此时，玩家 1 赢得了该场比赛)
    # |X| |O|
    # |O|O| |    // 玩家 1 在 (2, 1) 落子。
    # |X|X|X|


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
