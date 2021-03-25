#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:55:04
# @Last Modified : 2020-04-30 17:55:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
#  现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
#  所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
#  说明:
#
#
#  给出的房屋和供暖器的数目是非负数且不会超过 25000。
#  给出的房屋和供暖器的位置均是非负数且不会超过10^9。
#  只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
#  所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
#  示例 1:
#
#
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
#  示例 2:
#
#
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#  Related Topics 二分查找
#  👍 138 👎 0

"""

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
