#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-28 22:43:30
# @Last Modified : 2020-04-28 22:43:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            vp2, vp3, vp5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(vp2, vp3, vp5)
            if vp2 == dp[i]:
                p2 += 1
            if vp3 == dp[i]:
                p3 += 1
            if vp5 == dp[i]:
                p5 += 1
        return dp[n - 1]


sol = Solution()


@pytest.mark.parametrize("args,expected", [
    (1, 1),
    pytest.param(10, 12),
])
def test_solutions(args, expected):
    assert sol.nthUglyNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "-v", "--color=yes", __file__])
