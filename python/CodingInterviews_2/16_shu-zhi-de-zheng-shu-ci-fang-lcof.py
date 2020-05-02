#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 21:44:10
# @Last Modified : 2020-05-02 21:44:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def myPow(self, x: float, n: int) -> float:
        def helper(x,abs_n):
            if abs_n == 0:
                return 1
            if abs_n == 1:
                return x
            ans = helper(x, abs_n >> 1)
            ans *= ans
            if abs_n & 0b1 == 1:
                ans *= x
            return ans
        res = helper(x,abs(n))
        if n<0:
            res=1.0/res
        return res


@pytest.mark.parametrize("x,n,expected", [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25),
    (8.95371, -1,0.1116855),
])
def test_solutions(x, n, expected):
    assert Solution().myPow(x, n) == pytest.approx(expected, 0.001)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
