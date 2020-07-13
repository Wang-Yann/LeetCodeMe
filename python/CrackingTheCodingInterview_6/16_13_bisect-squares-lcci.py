#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 17:03:29
# @Last Modified : 2020-07-13 17:03:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。 
# 
#  每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2
# ]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点
# ）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。
#  
# 
#  若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。 
# 
#  示例： 
# 
#  输入：
# square1 = {-1, -1, 2}
# square2 = {0, -1, 2}
# 输出： {-1,0,2,0}
# 解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
#  
# 
#  提示： 
# 
#  
#  square.length == 3 
#  square[2] > 0 
#  
#  Related Topics 几何 
#  👍 2 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        # 分别计算出中心点center1和center2
        center1 = [square1[0] + square1[2] / 2, square1[1] + square1[2] / 2]
        center2 = [square2[0] + square2[2] / 2, square2[1] + square2[2] / 2]

        # 处理两种同轴的特殊情况
        # 同竖轴
        if center1[0] == center2[0]:
            return [center1[0], min(square1[1], square2[1]), center2[0],
                    max(square1[1] + square1[2], square2[1] + square2[2])]
        # 同横轴
        if center1[1] == center2[1]:
            return [min(square1[0], square2[0]), center1[1], max(square1[0] + square1[2], square2[0] + square2[2]),
                    center2[1]]

        # 判断是偏横着还是偏竖着穿过(斜率绝对值|k|<1横穿，否则竖穿)
        if abs((center2[1] - center1[1]) / (center2[0] - center1[0])) < 1:
            minX = min(square1[0], square2[0])
            maxX = max(square1[0] + square1[2], square2[0] + square2[2])
            leftY = center1[1] + (center2[1] - center1[1]) * (minX - center1[0]) / (center2[0] - center1[0])
            rightY = center1[1] + (center2[1] - center1[1]) * (maxX - center1[0]) / (center2[0] - center1[0])
            return [minX, leftY, maxX, rightY]
        else:
            minY = min(square1[1], square2[1])
            maxY = max(square1[1] + square1[2], square2[1] + square2[2])
            downX = center1[0] + (center2[0] - center1[0]) * (minY - center1[1]) / (center2[1] - center1[1])
            upX = center1[0] + (center2[0] - center1[0]) * (maxY - center1[1]) / (center2[1] - center1[1])
            return [downX, minY, upX, maxY] if downX < upX else [upX, maxY, downX, minY]

        return []


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(square1=[-1, -1, 2], square2=[0, -1, 2]), [-1, 0, 2, 0]],
])
def test_solutions(kw, expected):
    assert Solution().cutSquares(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
