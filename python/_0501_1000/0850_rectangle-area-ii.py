#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们给出了一个（轴对齐的）矩形列表 rectangles 。 对于 rectangle[i] = [x1, y1, x2, y2]，其中（x1，y1）是矩形
#  i 左下角的坐标，（x2，y2）是该矩形右上角的坐标。 
# 
#  找出平面中所有矩形叠加覆盖后的总面积。 由于答案可能太大，请返回它对 10 ^ 9 + 7 取模的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# 输出：6
# 解释：如图所示。
#  
# 
#  示例 2： 
# 
#  输入：[[0,0,1000000000,1000000000]]
# 输出：49
# 解释：答案是 10^18 对 (10^9 + 7) 取模的结果， 即 (10^9)^2 → (-7)^2 = 49 。
#  
# 
#  提示： 
# 
#  
#  1 <= rectangles.length <= 200 
#  rectanges[i].length = 4 
#  0 <= rectangles[i][j] <= 10^9 
#  矩形叠加覆盖后的总面积不会超越 2^63 - 1 ，这意味着可以用一个 64 位有符号整数来保存面积结果。 
#  
#  Related Topics 线段树 Line Sweep

"""

import functools
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class SegmentTree(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) >> 1

    @property
    def left(self):
        self._left = self._left or SegmentTree(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or SegmentTree(self.mid, self.end)
        return self._right

    def update(self, X, i, j, val):
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(X, i, min(self.mid, j), val)
            self.right.update(X, max(self.mid, i), j, val)
        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total
        return self.total


class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/problems/rectangle-area-ii/solution/ju-xing-mian-ji-ii-by-leetcode/
        线性扫描+线段树
        """
        OPEN, CLOSE = 1, -1
        events = []
        X_set = set()
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
            X_set.add(x1)
            X_set.add(x2)
        events.sort()
        X = sorted(X_set)
        xi = {x:i for i, x in enumerate(X)}
        st = SegmentTree(0, len(X) - 1)
        res = 0
        cur_x_sum = 0
        cur_y = events[0][0]
        for y, typ, x1, x2 in events:
            res += cur_x_sum * (y - cur_y)
            cur_x_sum = st.update(X, xi[x1], xi[x2], typ)
            cur_y = y
        return res % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    TLE
    """

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        容斥原理
        """

        def intersect(rec1, rec2):
            return [max(rec1[0], rec2[0]),
                    max(rec1[1], rec2[1]),
                    min(rec1[2], rec2[2]),
                    min(rec1[3], rec2[3])]

        def area(rec):
            dx = max(0, rec[2] - rec[0])
            dy = max(0, rec[3] - rec[1])
            return dx * dy

        ans = 0
        for size in range(1, len(rectangles) + 1):
            for group in itertools.combinations(rectangles, size):
                ans += (-1) ** (size + 1) * area(functools.reduce(intersect, group))
        return ans % (10 ** 9 + 7)


@pytest.mark.parametrize("args,expected", [
    ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
    pytest.param([[0, 0, 1000000000, 1000000000]], 49),
])
def test_solutions(args, expected):
    assert Solution().rectangleArea(args) == expected
    assert Solution1().rectangleArea(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
