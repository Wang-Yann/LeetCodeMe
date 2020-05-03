#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:24:14
# @Last Modified : 2020-05-03 14:24:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        将车辆按照起始位置排序后，我们顺序扫描这些车辆。如果相邻的两辆车，前者比后者行驶到终点需要的时间短，那么后者永远追不上前者，
        即从后者开始的若干辆车辆会组成一个新的车队；
        如果前者不比后者行驶到终点需要的时间短，那么后者可以在终点前追上前者，并和前者形成车队。此时我们将后者到达终点的时间置为前者到达终点的时间。
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans, cur = 0, 0
        for t in reversed(times):
            if t > cur:
                ans += 1
                cur = t
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().carFleet(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
