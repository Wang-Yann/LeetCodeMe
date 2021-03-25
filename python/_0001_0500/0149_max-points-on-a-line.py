#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 15:42:27
# @Last Modified : 2020-05-04 15:42:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
#
#  示例 1:
#
#  输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
#  示例 2:
#
#  输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#  Related Topics 哈希表 数学
#  👍 162 👎 0

import collections
from typing import List

import pytest


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        """TODO"""
        from fractions import Fraction
        Point = collections.namedtuple("Point", "x,y")
        points = [Point(*args) for args in points]
        max_points = 0
        for i, start in enumerate(points):
            # 斜率
            slope_count, same = collections.defaultdict(int), 1
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    slope = float("inf")
                    if start.x - end.x != 0:
                        slope = Fraction((start.y - end.y), (start.x - end.x))
                    slope_count[slope] += 1
            current_max = same
            # print("Same| slope | ", same, slope_count)
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)
            max_points = max(max_points, current_max)
        return max_points


@pytest.mark.parametrize("args,expected", [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([[0, 0], [94911151, 94911150], [94911152, 94911151]], 2),
    pytest.param([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
])
def test_solutions(args, expected):
    assert Solution().maxPoints(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
