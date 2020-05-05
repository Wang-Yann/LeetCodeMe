#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:51:01
# @Last Modified : 2020-05-05 14:51:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def findNthDigit(self, n: int) -> int:
        """https://leetcode-cn.com/problems/nth-digit/solution/xiang-jie-zhao-gui-lu-by-z1m/"""
        n -= 1
        for digits in range(1, 11):
            first_num = 10 ** (digits - 1)
            if n < 9 * first_num * digits:
                res_num = str(first_num + n // digits)
                return int(res_num[n % digits])
            n -= 9 * first_num * digits


class Solution1:

    def findNthDigit(self, n: int) -> int:
        num = 9
        digit = 1
        n-=1
        while n - num * digit > 0:
            n -= num * digit
            num *= 10
            digit += 1
        a, b = divmod(n, digit)
        return int(str(10 ** (digit - 1) + a)[b])


@pytest.mark.parametrize("args,expected", [
    (3, 3),
    pytest.param(11, 0),
])
def test_solutions(args, expected):
    assert Solution().findNthDigit(args) == expected
    assert Solution1().findNthDigit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
