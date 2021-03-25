#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 22:23:28
# @Last Modified : 2020-04-15 22:23:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  注意数组中可能存在重复的元素。
#
#  示例 1：
#
#  输入: [1,3,5]
# 输出: 1
#
#  示例 2：
#
#  输入: [2,2,2,0,1]
# 输出: 0
#
#  说明：
#
#
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#  Related Topics 数组 二分查找
#  👍 131 👎 0

"""

from typing import List

import pytest


class Solution:

    def findMin(self, nums: List[int]) -> int:

        """
        例如 [1, 0, 1, 1, 1]  和 [1, 1, 1, 0, 1]  ，在 left = 0, right = 4, mid = 2 时，
        无法判断  mid 在哪个排序数组中。

        我们采用 right = right - 1 解决此问题，证明：
            此操作不会使数组越界：因为迭代条件保证了 right > left >= 0；
            此操作不会使最小值丢失：假设 nums[right] 是最小值，有两种情况：
            若 nums[right] 是唯一最小值：那就不可能满足判断条件 nums[mid] == nums[right]，
            因为 mid < right（left != right 且 mid = (left + right) // 2 向下取整）；
            若 nums[right]  不是唯一最小值，由于 mid < right 而 nums[mid] == nums[right]，
            即还有最小值存在于 [left, right - 1]  区间，因此不会丢失最小值。
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1  # key point

        return nums[left]


@pytest.mark.parametrize("args,expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([1, 2], 1),
    ([2, 2, 2, 0, 1], 0),
    ([1, 0, 1, 1, 1], 0),
    ([1, 1, 1, 0, 1], 0),
    ([1, 1, 1, 1, 1], 1),
])
def test_solutions(args, expected):
    assert Solution().findMin(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
