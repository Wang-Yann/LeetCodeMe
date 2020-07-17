#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:12:47
# @Last Modified : 2020-04-06 14:12:47
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
"""
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例：
#
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针
#  👍 1641 👎 0

"""
from typing import List

import pytest

from sample_datas import BIG_11


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        start, end = 0, length - 1
        cur_max_area = 0
        while start < end:
            area = (end - start) * min(height[end], height[start])
            cur_max_area = max(cur_max_area, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return cur_max_area


@pytest.mark.parametrize("args,expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    (BIG_11.BIG_CASE, 48267879),
])
def test_solutions(args, expected):
    assert Solution().maxArea(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
