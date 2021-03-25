#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y
# 1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。 
# 
#  如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。 
# 
#  换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# 输出：true
# 解释：圆和矩形有公共点 (1,0) 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= radius <= 2000 
#  -10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4 
#  x1 < x2 
#  y1 < y2 
#  
#  Related Topics 几何

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        https://leetcode-cn.com/problems/circle-and-rectangle-overlapping/solution/circle-and-rectangle-overlapping-by-ikaruga/
        先计算矩形中心，边长；
        把矩形中心，圆心投影到坐标轴上；
        计算矩形中心与圆心在坐标轴上的距离；
        判断，圆心超出矩形的距离是否小于等于圆的半径;
        """
        x0 = 0.5 * (x1 + x2)
        y0 = 0.5 * (y1 + y2)
        p = abs(x_center - x0), abs(y_center - y0)
        q = x2 - x0, y2 - y0
        u = max(p[0] - q[0], 0.0), max(p[1] - q[1], 0.0)
        return u[0] ** 2 + u[1] ** 2 <= radius * radius


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1), True],
    [dict(radius=1, x_center=0, y_center=0, x1=-1, y1=0, x2=0, y2=1), True],
    [dict(radius=1, x_center=1, y_center=1, x1=-3, y1=-3, x2=3, y2=3), True],
    [dict(radius=1, x_center=1, y_center=1, x1=1, y1=-3, x2=2, y2=-1), False],
])
def test_solutions(kw, expected):
    assert Solution().checkOverlap(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
