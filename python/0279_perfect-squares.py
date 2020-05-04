#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 22:15:50
# @Last Modified : 2020-05-04 22:15:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math

import pytest


class Solution:

    def numSquares(self, n: int) -> int:
        """
        DP
        numSquares(n)=min(numSquares(n-k) + 1)
        """
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]


@pytest.mark.parametrize("args,expected", [
    (12, 3),
    pytest.param(13, 2),
])
def test_solutions(args, expected):
    assert Solution().numSquares(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
