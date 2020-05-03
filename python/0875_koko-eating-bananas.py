#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:48:19
# @Last Modified : 2020-05-03 14:48:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math
from typing import List

import pytest


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """ Math.ceil(p / K) = ((p-1) // K) + 1"""
        def possible(K):
            # Can Koko eat all bananas in H hours with eating speed K?
            return sum([math.ceil(p/K) for p in piles]) <= H

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) >> 1
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kwargs,expected", [
    (dict(piles=[3, 6, 7, 11], H=8), 4),
    (dict(piles=[30, 11, 23, 4, 20], H=5), 30),
    (dict(piles=[30, 11, 23, 4, 20], H=6), 23),
])
def test_solutions(kwargs, expected):
    assert Solution().minEatingSpeed(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
