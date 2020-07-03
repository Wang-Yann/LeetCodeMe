#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为
#  x、纵坐标为 y 的点。 
# 
#  请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= coordinates.length <= 1000 
#  coordinates[i].length == 2 
#  -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4 
#  coordinates 中不含重复的点 
#  
#  Related Topics 几何 数组 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    ), True),
    pytest.param(dict(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]), False),
    pytest.param(dict(coordinates=[[2, 4], [2, 5], [2, 8]]), True),
    pytest.param(dict(coordinates=[[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]]), True),
])
def test_solutions(kwargs, expected):
    assert Solution().checkStraightLine(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
