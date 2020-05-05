#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 13:26:50
# @Last Modified : 2020-05-05 13:26:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return z == 0 or ((x + y >= z) and z % (gcd(x, y)) == 0)


class Solution1:

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """
        GOOD
        """
        # (X 壶中的水量，以及 Y 壶中的水量。)
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            delta_x = min(remain_x, y - remain_y)
            stack.append((remain_x - delta_x, remain_y + delta_x))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            delta_y = min(remain_y, x - remain_x)
            stack.append((remain_x + delta_y, remain_y - delta_y))
        return False


@pytest.mark.parametrize("kwargs,expected", [
    (dict(x=3, y=5, z=4), True),
    pytest.param(dict(x=2, y=6, z=5), False),
])
def test_solutions(kwargs, expected):
    assert Solution().canMeasureWater(**kwargs) == expected
    assert Solution1().canMeasureWater(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
