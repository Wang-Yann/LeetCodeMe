#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 12:18:05
# @Last Modified : 2020-04-12 12:18:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。
#
#  要求浮点型误差不超过10^-6。若有多个交点（线段重叠）则返回 X 值最小的点，X 坐标相同则返回 Y 值最小的点。
#
#
#
#  示例 1：
#
#  输入：
# line1 = {0, 0}, {1, 0}
# line2 = {1, 1}, {0, -1}
# 输出： {0.5, 0}
#
#
#  示例 2：
#
#  输入：
# line1 = {0, 0}, {3, 3}
# line2 = {1, 1}, {2, 2}
# 输出： {1, 1}
#
#
#  示例 3：
#
#  输入：
# line1 = {0, 0}, {1, 1}
# line2 = {1, 0}, {2, 1}
# 输出： {}，两条线段没有交点
#
#
#
#
#  提示：
#
#
#  坐标绝对值不会超过 2^7
#  输入的坐标均是有效的二维坐标
#
#  Related Topics 几何 数学
#  👍 55 👎 0


from typing import List

import pytest


class Solution:

    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        """
        k = (y2-y1)/(x2-x1)
        b = (x2*y1-x1*y2)/(x2-x1)

        一般式:Ax+By+C=0(A、B不同时为0)【适用于所有直线】

        直线的一般方程为F(x) = ax + by + c = 0。既然我们已经知道直线的两个点，假设为(x0,y0), (x1, y1)，
            那么可以得到a = y0 – y1, b = x1 – x0, c = x0y1 – x1y0。

        因此我们可以将两条直线分别表示为

        F0(x) = a0*x + b0*y + c0 = 0, F1(x) = a1*x + b1*y + c1 = 0

        那么两条直线的交点应该满足

        a0*x + b0*y +c0 = a1*x + b1*y + c1

        由此可推出

        x = (b0*c1 – b1*c0)/D
        y = (a1*c0 – a0*c1)/D
        D = a0*b1 – a1*b0， (D为0时，表示两直线重合/平行)
        """
        if start1[0] > start2[0] or start1[0] == start2[0] and start1[1] > start2[1]:
            start1, end1, start2, end2 = start2, end2, start1, end1
        A1, B1, C1 = start1[1] - end1[1], end1[0] - start1[0], start1[0] * end1[1] - start1[1] * end1[0]
        A2, B2, C2 = start2[1] - end2[1], end2[0] - start2[0], start2[0] * end2[1] - start2[1] * end2[0]
        D = A1 * B2 - A2 * B1
        if D == 0:
            # print("k==0 | ", A1, B1, C1,"|", A2, B2, C2 )
            if B1 == 0 and B2 == 0 and (A1 * C2 - A2 * C1) == 0 and end1[1] >= start2[1]:
                return start2
            elif (B1 != 0 and B2 != 0) and B1 * C2 - B2 * C1 == 0 and end1[0] >= start2[0]:
                return start2
        if D != 0:
            intersect = [(B1 * C2 - B2 * C1) / D, (A2 * C1 - A1 * C2) / D]
            # print("k!=0",intersect)
            range1_x = (start1[0], end1[0]) if start1[0] <= end1[0] else (end1[0], start1[0])
            range1_y = (start1[1], end1[1]) if start1[1] <= end1[1] else (end1[1], start1[1])
            range2_x = (start2[0], end2[0]) if start2[0] <= end2[0] else (end2[0], start2[0])
            range2_y = (start2[1], end2[1]) if start2[1] <= end2[1] else (end2[1], start2[1])

            if range1_x[0] <= intersect[0] <= range1_x[1] \
                and range2_x[0] <= intersect[0] <= range2_x[1] \
                and range1_y[0] <= intersect[1] <= range1_y[1] \
                and range2_y[0] <= intersect[1] <= range2_y[1]:
                return intersect
        return []


@pytest.mark.parametrize("args,expected", [
    [([0, 0], [1, 0], [1, 1], [0, -1]), [0.5, 0]],
    [([0, 0], [3, 3], [1, 1], [2, 2]), [1, 1]],
    [([0, 0], [1, 1], [1, 0], [2, 1]), []],
    [([0, 0], [0, 1], [0, 2], [0, 3]), []],
])
def test_solutions(args, expected):
    assert Solution().intersection(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
