#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:46:09
# @Last Modified : 2020-04-30 15:46:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
TARGET = 6


def guess(num: int) -> int:
    if num < TARGET:
        return 1
    elif num > TARGET:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) >> 1
            if guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == -1:
                r = mid - 1
            else:
                return mid
        return l


@pytest.mark.parametrize("args,expected", [
    (10, 6)
])
def test_solutions(args, expected):
    assert Solution().guessNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
