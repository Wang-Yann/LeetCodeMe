#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 00:05:35
# @Last Modified : 2020-05-02 00:05:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否
# 则返回 -1。
#
#
# 示例 1:
#
#  输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
#
#  示例 2:
#
#  输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#
#
#
#  提示：
#
#
#  你可以假设 nums 中的所有元素是不重复的。
#  n 将在 [1, 10000]之间。
#  nums 的每个元素都将在 [-9999, 9999]之间。
#
#  Related Topics 二分查找
#  👍 140 👎 0

from typing import List

import pytest


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
            else:
                return mid
        return -1


class Solution1:

    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            if l > r:
                return -1
            mid = (l + r) >> 1
            if nums[mid] < target:
                return binary_search(mid + 1, r)
            elif nums[mid] > target:
                return binary_search(l, mid - 1)
            else:
                return mid

        return binary_search(0, len(nums) - 1)


@pytest.mark.parametrize("nums,target,expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    pytest.param([-1, 0, 3, 5, 9, 12], 15, -1),
])
def test_solutions(nums, target, expected):
    assert Solution().search(nums, target) == expected
    assert Solution1().search(nums, target) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
