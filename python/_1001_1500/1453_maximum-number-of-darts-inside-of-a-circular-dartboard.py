#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 23:58:26
# @Last Modified : 2020-07-05 23:58:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。 
# 
#  投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 r 。 
# 
#  请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# 输出：4
# 解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# 输出：5
# 解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。 
# 
#  示例 3： 
# 
#  输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 100 
#  points[i].length == 2 
#  -10^4 <= points[i][0], points[i][1] <= 10^4 
#  1 <= r <= 5000 
#  
#  Related Topics 几何 
#  👍 17 👎 0

"""
import itertools
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numPoints(self, points: List[List[int]], r: int) -> int:
        """
        O(n**2*log(N))
        angular sweep
        https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/discuss/636345/Python-O(n3)-and-O(n2logn)-solution-explained-in-detail-with-pictures
        """
        ans = 1
        for x, y in points:
            angles = []
            for x1, y1 in points:
                d = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                if (x1 != x or y1 != y) and d <= 2 * r:
                    angle = math.atan2(y1 - y, x1 - x)
                    delta = math.acos(1.0 * d / (2 * r))
                    angles.append((angle - delta, 1))  # entry
                    angles.append((angle + delta, -1))  # exit
            angles.sort(key=lambda x:(x[0], -x[1]))
            val = 1
            for _, entry in angles:
                val = val + entry
                ans = max(ans, val)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def numPoints(self, points: List[List[int]], r: int) -> int:
        """
        O(n**3)
        https://stackoverflow.com/questions/3229459/algorithm-to-cover-maximal-number-of-points-with-one-circle-of-given-radius/3229582#3229582
        """
        res = 1
        A = points
        for (x1, y1), (x2, y2) in itertools.combinations(A, 2):
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) / 4.0
            if d > r * r:
                continue
            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
            res = max(res, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in A))
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(points=[[-2, 0], [2, 0], [0, 2], [0, -2]], r=2), 4),
    pytest.param(dict(points=[[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5), 5),
    pytest.param(dict(points=[[-2, 0], [2, 0], [0, 2], [0, -2]], r=1), 1),
    pytest.param(dict(points=[[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], r=2), 4),
    pytest.param(dict(points=[[4, -4], [-2, 0], [0, 2], [-3, 1], [2, 3], [2, 4], [1, 1]], r=3), 6),
])
def test_solutions(kwargs, expected):
    assert Solution().numPoints(**kwargs) == expected
    assert Solution1().numPoints(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
