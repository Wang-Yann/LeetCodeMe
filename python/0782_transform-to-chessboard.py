#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 19:34:23
# @Last Modified : 2020-05-05 19:34:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import collections
from typing import List

import pytest


class Solution:

    def movesToChessboard(self, board: List[List[int]]) -> int:
        """
        HARD Need understand
        """
        N = len(board)
        ans = 0
        # For each count of lines from {rows, columns}...

        for count in (
                collections.Counter(map(tuple, board)),
                collections.Counter(zip(*board))
        ):
            # If there are more than 2 kinds of lines,
            # or if the number of kinds is not appropriate ...
            if len(count) != 2 or sorted(count.values()) != [N // 2, (N + 1) // 2]:
                return -1
            # If the lines are not opposite each other, impossible
            line1, line2 = count
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1
            # +(True)=1
            # starts = what could be the starting value of line1
            # If N is odd, then we have to start with the more
            # frequent element
            starts = [+(line1.count(1) * 2 > N)] if N % 2 == 1 else [0, 1]

            # To transform line1 into the ideal line [i%2 for i ...],
            # we take the number of differences and divide by two
            ans += min(sum([(i - x) % 2 for i, x in enumerate(line1, start)]) for start in starts) // 2
        return ans


@pytest.mark.parametrize("args,expected", [
    ([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]], 2),
    ([[1, 0], [1, 0]], -1),
    pytest.param([[0, 1], [1, 0]], 0),
])
def test_solutions(args, expected):
    assert Solution().movesToChessboard(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
