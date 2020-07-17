#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:09:36
# @Last Modified : 2020-05-05 17:09:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
#  示例 1:
#
#
# 输入: [1,2,3]
# 输出: 6
#
#
#  示例 2:
#
#
# 输入: [1,2,3,4]
# 输出: 24
#
#
#  注意:
#
#
#  给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
#  输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
#
#  Related Topics 数组 数学
#  👍 142 👎 0

"""

from typing import List

import pytest


class Solution:

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        length = len(nums)
        if length < 3:
            return 0
        return max([
            nums[-1] * nums[-2] * nums[0],
            nums[-1] * nums[0] * nums[1],
            nums[0] * nums[1] * nums[2]
        ])


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 6),
    pytest.param([1, 2, 3, 4], 24),
])
def test_solutions(args, expected):
    assert Solution().maximumProduct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
