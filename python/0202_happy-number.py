#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 09:27:54
# @Last Modified : 2020-04-30 09:27:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def isHappy(self, n: int) -> bool:
        def getBitPow(x):
            total_sum = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total_sum += digit ** 2
            return total_sum

        lookup = set()
        while n != 1 and n not in lookup:
            lookup.add(n)
            n = getBitPow(n)
        return n == 1


@pytest.mark.parametrize("args,expected", [
    [19, True],
    [1, True]
])
def test_solutions(args, expected):
    assert Solution().isHappy(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
