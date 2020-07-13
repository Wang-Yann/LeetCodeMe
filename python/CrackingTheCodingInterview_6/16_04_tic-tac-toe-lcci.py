#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:53:26
# @Last Modified : 2020-07-13 14:53:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。 
# 
#  以下是井字游戏的规则： 
# 
#  
#  玩家轮流将字符放入空位（" "）中。 
#  第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。 
#  "X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。 
#  当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。 
#  当所有位置非空时，也算为游戏结束。 
#  如果游戏结束，玩家不允许再放置字符。 
#  
# 
#  如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "P
# ending"。 
# 
#  示例 1： 
# 
#  输入： board = ["O X"," XO","X O"]
# 输出： "X"
#  
# 
#  示例 2： 
# 
#  输入： board = ["OOX","XXO","OXO"]
# 输出： "Draw"
# 解释： 没有玩家获胜且不存在空位
#  
# 
#  示例 3： 
# 
#  输入： board = ["OOX","XXO","OX "]
# 输出： "Pending"
# 解释： 没有玩家获胜且仍存在空位
#  
# 
#  提示： 
# 
#  
#  1 <= board.length == board[i].length <= 100 
#  输入一定遵循井字棋规则 
#  
#  Related Topics 数组 
#  👍 10 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        N = len(board)

        def check(char):
            s = char * N
            return any((
                any(row == s for row in board),
                any(col == s for col in map(''.join, zip(*board))),
                all(board[i][i] == char for i in range(N)),
                all(board[i][N - i - 1] == char for i in range(N))
            ))

        if check('X'):
            return 'X'
        elif check('O'):
            return 'O'
        elif ' ' in ''.join(board):
            return 'Pending'
        return 'Draw'


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(board=["O X", " XO", "X O"]), "X"],
    [dict(board=["OOX", "XXO", "OXO"]), "Draw"],
    [dict(board=["OOX", "XXO", "OX "]), "Pending"],
])
def test_solutions(kw, expected):
    assert Solution().tictactoe(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
