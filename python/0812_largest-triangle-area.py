#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 21:03:39
# @Last Modified : 2020-05-05 21:03:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import itertools
from typing import List

import pytest


class Solution:

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        海伦公式
        p=(a+b+c)/2

        S**2 = p*(p-1)*(p-b)*(p-c)

        鞋带公式

        S = 1/2* |(x1*y2+x2*y3+x3*y1 -( y1*x2+y2*x3+y3*x1 )     |


        """

        def area(a, b, c):
            return 0.5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] -
                             b[0] * a[1] - c[0] * b[1] - a[0] * c[1])

        return max(area(*points_group) for points_group in itertools.combinations(points, 3))


@pytest.mark.parametrize("args,expected", [
    ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2),
])
def test_solutions(args, expected):
    assert Solution().largestTriangleArea(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
