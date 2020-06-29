#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。 
# 
#  如果没有任何矩形，就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。 
# 
#  示例 2： 
# 
#  
# 
#  输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 50 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  所有的点都是不同的。 
#  与真实值误差不超过 10^-5 的答案将视为正确结果。 
#  
#  Related Topics 几何 数学

"""

import collections
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        """
        暴力枚举中心
        点对 PQ 按照它们的中点 C 与距中点距离 r = dist(P, C) 分类
        """
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius_complex = center - P
            radius_square = radius_complex*radius_complex.conjugate()
            seen[center, radius_square].append(P)
        # print(seen)
        ans = float("inf")
        for (center, radius_square), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                # print(P,Q,abs(P-Q),P - (2*center - Q))
                # 注意理解复数集合意义,画下图
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))
        return ans if ans != float("inf") else 0


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [2, 1], [1, 0], [0, 1]], 2.000),
    ([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]], 1.000),
    ([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]], 0),
    ([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]], 2.0),
])
def test_solutions(args, expected):
    assert Solution().minAreaFreeRect(args) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
