#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:13:45
# @Last Modified : 2020-05-10 18:13:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def findNthDigit(self, n: int) -> int:
        num = 9
        digit = 1
        n -= 1
        while n - num * digit > 0:
            n -= num * digit
            num *= 10
            digit += 1
        times, rest = divmod(n, digit)
        # print("times,rest| digit,num", times, rest, digit, num)
        return int(str(10 ** (digit - 1) + times)[rest])


@pytest.mark.parametrize("args,expected", [
    # (3, 3),
    (1013, 7),
    # pytest.param(11, 0),
])
def test_solutions(args, expected):
    assert Solution().findNthDigit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
