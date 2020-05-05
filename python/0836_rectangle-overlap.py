#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 21:29:12
# @Last Modified : 2020-05-05 21:29:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        矩形 rec1 在矩形 rec2 的左侧；
        矩形 rec1 在矩形 rec2 的右侧；
        矩形 rec1 在矩形 rec2 的上方；
        矩形 rec1 在矩形 rec2 的下方
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3]  # top
                    )

class Solution1(object):
    """
    检查投影
    如果两个矩形重叠，那么它们重叠的区域一定也是一个矩形，那么这代表了两个矩形与 xx 轴平行的边（水平边）投影到 xx 轴上时会有交集，与 yy 轴平行的边（竖直边）投影到 yy 轴上时也会有交集

    """
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))



@pytest.mark.parametrize("kwargs,expected", [
    (dict(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]), True),
    (dict(rec1=[7, 8, 13, 15], rec2=[10, 8, 12, 20]), True),
    pytest.param(dict(rec1=[0, 0, 1, 1], rec2=[1, 0, 2, 1]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isRectangleOverlap(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
