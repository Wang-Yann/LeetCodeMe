#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 20:32:03
# @Last Modified : 2020-04-16 20:32:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 峰值元素是指其值大于左右相邻值的元素。
#
#  给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
#  数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
#  你可以假设 nums[-1] = nums[n] = -∞。
#
#  示例 1:
#
#  输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
#
#  示例 2:
#
#  输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
#
#
#  说明:
#
#  你的解法应该是 O(logN) 时间复杂度的。
#  Related Topics 数组 二分查找
#  👍 250 👎 0

"""

from typing import List

import pytest


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 1], {2}),
    ([1, 2, 1, 3, 5, 6, 4], {1, 5}),
])
def test_solutions(args, expected):
    assert Solution().findPeakElement(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
