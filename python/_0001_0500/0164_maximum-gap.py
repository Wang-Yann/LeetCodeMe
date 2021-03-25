#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 11:54:17
# @Last Modified : 2020-05-01 11:54:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
#  如果数组元素个数小于 2，则返回 0。
#
#  示例 1:
#
#  输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
#  示例 2:
#
#  输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
#  说明:
#
#
#  你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
#  请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
#
#  Related Topics 排序
#  👍 173 👎 0

"""

from typing import List

import pytest


class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        pre = nums[0]
        max_gap = float("-inf")
        for v  in nums:
            max_gap = max(max_gap,v-pre)
            pre =v
        return  max_gap


@pytest.mark.parametrize("args,expected", [
    ([3, 6, 9, 1], 3),
    pytest.param([10], 0),
])
def test_solutions(args, expected):
    assert Solution().maximumGap(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
