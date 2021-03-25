#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:57:41
# @Last Modified : 2020-05-05 16:57:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
#
#  一个点的坐标（x，y）由一个有两个整数的整数数组表示。
#
#  示例:
#
#
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True
#
#
#
#
#  注意:
#
#
#  所有输入整数都在 [-10000，10000] 范围内。
#  一个有效的正方形有四个等长的正长和四个等角（90度角）。
#  输入点没有顺序。
#
#  Related Topics 数学
#  👍 39 👎 0

"""

from typing import List

import pytest


class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        lookup = set([
            dist(p1, p2), dist(p1, p3), dist(p1, p4),
            dist(p2, p3), dist(p2, p4), dist(p3, p4)
        ])
        return 0 not in lookup and len(lookup) == 2


@pytest.mark.parametrize("kwargs,expected", [
    (dict(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]), True),
])
def test_solutions(kwargs, expected):
    assert Solution().validSquare(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
