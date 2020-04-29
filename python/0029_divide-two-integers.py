#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 13:42:09
# @Last Modified : 2020-04-29 13:42:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648,res),2147483647)


@pytest.mark.parametrize("args", [
    (10, 3, 3),
    (7, -3, -2),

])
def test_solution(args):
    sol = Solution()
    *args, expected = args
    assert sol.divide(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
