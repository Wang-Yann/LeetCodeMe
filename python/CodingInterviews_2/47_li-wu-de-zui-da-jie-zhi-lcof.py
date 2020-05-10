#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:51:41
# @Last Modified : 2020-05-10 18:51:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n+1) for _ in range(m +1)]
        for j in range(n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m-1][n-1]


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]
     ], 12),
    ([[1]],1)
])
def test_solutions(args, expected):
    assert Solution().maxValue(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
