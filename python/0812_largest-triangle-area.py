#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 21:03:39
# @Last Modified : 2020-05-05 21:03:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
#
#
#  注意:
#
#
#  3 <= points.length <= 50.
#  不存在重复的点。
#  -50 <= points[i][j] <= 50.
#  结果误差值在 10^-6 以内都认为是正确答案。
#
#  Related Topics 数学
#  👍 58 👎 0

"""

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
