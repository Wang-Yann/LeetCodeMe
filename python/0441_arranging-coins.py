#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:27:09
# @Last Modified : 2020-04-30 17:27:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n in (0, 1):
            return n
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            v = (1 + mid) * mid // 2
            if v < n:
                l = mid + 1
            elif v > n:
                r = mid - 1
            else:
                return mid
        return l-1


@pytest.mark.parametrize("args,expected", [
    (5, 2),
    (8, 3)
])
def test_solutions(args, expected):
    assert Solution().arrangeCoins(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
