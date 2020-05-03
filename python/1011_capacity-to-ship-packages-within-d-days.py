#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:26:34
# @Last Modified : 2020-05-03 16:26:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def is_possible(mid_d):
            res, cur = 1, 0
            for w in weights:
                if cur + w > mid_d:
                    res += 1
                    cur = 0
                cur += w
            return res <= D

        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) >> 1
            if is_possible(mid ):
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kwargs,expected", [
    (dict(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], D=5), 15),
    pytest.param(dict(weights=[3, 2, 2, 4, 1, 4], D=3), 6),
    pytest.param(dict(weights=[1, 2, 3, 1, 1], D=4), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().shipWithinDays(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
