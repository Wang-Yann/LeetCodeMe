#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。 
# 
#  如果没有任何矩形，就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 500 
#  0 <= points[i][0] <= 40000 
#  0 <= points[i][1] <= 40000 
#  所有的点都是不同的。 
#  
#  Related Topics 哈希表

"""
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        lookup = set()
        res = math.inf
        for x1, y1 in points:
            for x2, y2 in lookup:
                if (x1, y2) in lookup and (x2, y1) in lookup:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
            lookup.add((x1, y1))
        return res if res != math.inf else 0


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]], 4),
    ([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]], 2),
])
def test_solutions(args, expected):
    assert Solution().minAreaRect(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
