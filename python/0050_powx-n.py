#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 13:53:26
# @Last Modified : 2020-04-29 13:53:26
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        positive = 1 if n > 0 else -1
        res = 1
        while abs_n:
            if abs_n & 0b1:
                res *= x
            abs_n >>= 1
            x *= x
        if positive == -1:
            res = 1.0 / res
        return min(max(-2147483648, res), 2147483647)

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)



@pytest.mark.parametrize("args", [
    (2.0, 10, 1024.0),
    (2.10, 3, 9.2610),
    (2.0, -2, 0.25)
])
def test_solutions(args):
    *args, expected = args
    assert Solution().myPow(*args) == pytest.approx(expected, 0.001)
    assert Solution1().myPow(*args) == pytest.approx(expected, 0.001)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
