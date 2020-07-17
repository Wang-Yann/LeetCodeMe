#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 9:43 PM
# @Last Modified : 4/4/20 9:43 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
import bisect
from typing import List

import pytest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return 1 if target > nums[0] else 0
        i = 0
        j = 1
        while j < length:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[i] < target:
                if nums[j] < target:
                    i += 1
                    j += 1
                else:
                    return j
            else:
                return i
        return j

    def binarysearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def binarysearchRec(self, nums, target):
        return self.binarysearchRecurse(nums, target, 0, len(nums) - 1)

    def binarysearchRecurse(self, nums, target, low, high):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarysearchRecurse(nums, target, mid + 1, high)
        else:
            return self.binarysearchRecurse(nums, target, low, mid - 1)


class Solution1:

    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low = 0
        high = N - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


class Solution2:

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


@pytest.mark.parametrize("args,expected", [
    [([1, 3, 5, 6], 5), 2],
    [([1, 3, 5, 6], 2), 1],
    [([1, 3, 5, 6], 7), 4],
    [([1, 3, 5, 6], 0), 0]
])
def test_solutions(args, expected):
    assert Solution().searchInsert(*args) == expected
    assert Solution().searchInsert(*args) == expected
    assert Solution1().searchInsert(*args) == expected
    assert Solution2().searchInsert(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
