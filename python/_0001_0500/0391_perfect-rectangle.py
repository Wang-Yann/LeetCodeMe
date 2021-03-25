#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。 
# 
#  每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点
# 的坐标为 (2, 2) )。 
# 
#  
# 
#  示例 1: 
# 
#  rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
# 
# 返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
#  
# 
#  
# 
#  
# 
#  示例 2: 
# 
#  rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
# 
# 返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
#  
# 
#  
# 
#  
# 
#  示例 3: 
# 
#  rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
# 
# 返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
#  
# 
#  
# 
#  
# 
#  示例 4: 
# 
#  rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# 
# 返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
#  
#  Related Topics Line Sweep

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        left = min(rec[0] for rec in rectangles)
        bottom = min(rec[1] for rec in rectangles)
        right = max(rec[2] for rec in rectangles)
        top = max(rec[3] for rec in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            # 1 2 4 8 分别指带四个顶点，若有重合  不完美
            for p, q in zip(((l, b), (r, b), (l, t), (r, t)), (1, 2, 4, 8)):
                if points[p] & q:
                    return False
                points[p] |= q

        for px, py in points:
            # 出去顶点外
            if left < px < right or bottom < py < top:
                # 3,12,5,10,15分别代表该点出现2次和4次
                if points[(px, py)] not in (3, 5, 10, 12, 15):
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        rectangles=[
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [3, 2, 4, 4],
            [1, 3, 2, 4],
            [2, 3, 3, 4]
        ]

    ), True),
    (dict(
        rectangles=[
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [3, 2, 4, 4]
        ]

    ), False),
    (dict(
        rectangles=[
            [1, 1, 3, 3],
            [3, 1, 4, 2],
            [1, 3, 2, 4],
            [2, 2, 4, 4]
        ]

    ), False),
    pytest.param(dict(
        rectangles=[
            [1, 1, 2, 3],
            [1, 3, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 4, 4]
        ]

    ), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isRectangleCover(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
