#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 20:03:09
# @Last Modified : 2020-05-05 20:03:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def validTicTacToe(self, board: List[str]) -> bool:
        def win(player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])

        FIRST, SECOND = "XO"
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)
        if o_count not in (x_count, x_count - 1):
            return False
        if win(FIRST) and x_count - 1 != o_count:
            return False
        if win(SECOND) and x_count != o_count:
            return False
        return True


@pytest.mark.parametrize("args,expected", [
    (["O  ", "   ", "   "], False),
    (["XO  ", "   ", "   "], True),
    (["XXX", "   ", "OOO"], False),
    (["XOX", "O O", "XOX"], True),
    pytest.param(["XOX", " X ", "   "], False),
])
def test_solutions(args, expected):
    assert Solution().validTicTacToe(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
