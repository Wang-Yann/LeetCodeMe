#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。 
# 
#  给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[1,1],[2,3],[3,2]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：[[1,1],[2,2],[3,3]]
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  points.length == 3 
#  points[i].length == 2 
#  0 <= points[i][j] <= 100 
#  
#  Related Topics 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) - \
               (points[0][0] - points[2][0]) * (points[0][1] - points[1][1]) != 0


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [[1, 1], [2, 3], [3, 2]]
            , True),
    pytest.param([[1, 1], [2, 2], [3, 3]], False),
])
def test_solutions(args, expected):
    assert Solution().isBoomerang(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
