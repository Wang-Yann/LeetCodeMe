#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:55:04
# @Last Modified : 2020-04-30 17:55:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import bisect
from typing import List

import pytest


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """Good"""
        heaters.sort()
        min_radius = 0
        for house in houses:
            equal_or_larger = bisect.bisect_left(heaters, house)
            cur_radius = float("inf")
            if equal_or_larger != len(heaters):
                cur_radius = heaters[equal_or_larger] - house
            if equal_or_larger != 0:
                smaller = equal_or_larger - 1
                cur_radius = min(cur_radius, house - heaters[smaller])
            min_radius = max(min_radius, cur_radius)
        return min_radius


@pytest.mark.parametrize("args,expected", [
    [([1, 2, 3], [2]), 1],
    [([1, 2, 3, 4], [1, 4]), 1],
])
def test_solutions(args, expected):
    assert Solution().findRadius(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
