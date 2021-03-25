#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 19:22:34
# @Last Modified : 2020-07-27 19:22:34
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？ 
# 
#  示例 1： 
# 
#  输入: [[1,1],[-1,1]]
# 输出: true
#  
# 
#  示例 2： 
# 
#  输入: [[1,1],[-1,-1]]
# 输出: false 
# 
#  拓展： 
# 你能找到比 O(n2) 更优的解法吗? 
#  Related Topics 哈希表 数学 
#  👍 9 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        groups_by_y = collections.defaultdict(set)
        left, right = float("inf"), float("-inf")
        for x, y in points:
            groups_by_y[y].add(x)
            left, right = min(left, x), max(right, x)
        mid = left + right
        for group in groups_by_y.values():
            for x in group:
                if mid - x not in group:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(points=[[1, 1], [-1, 1]]), True],
    [dict(points=[[1, 1], [-1, -1]]), False],
])
def test_solutions(kw, expected):
    assert Solution().isReflected(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
