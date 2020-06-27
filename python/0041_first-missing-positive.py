#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-07 21:13:53
# @Last Modified : 2020-04-07 21:13:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#
#
#  示例 1:
#
#  输入: [1,2,0]
# 输出: 3
#
#
#  示例 2:
#
#  输入: [3,4,-1,1]
# 输出: 2
#
#
#  示例 3:
#
#  输入: [7,8,9,11,12]
# 输出: 1
#
#
#
#
#  提示：
#
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
#  Related Topics 数组

https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
"""

from typing import List

import pytest


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        # 3 应该放在索引为 2 的地方
        # 4 应该放在索引为 3 的地方

        while i <= len(nums) - 1:
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            if nums[i] > 0 and nums[i] - 1 < length and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        # print(nums)
        for i, integer in enumerate(nums):
            if integer != i + 1:
                return i + 1
        return length + 1


class Solution1:

    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1

        for i in range(N):
            num = abs(nums[i])
            if num <= N:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(N):
            if nums[i] > 0:
                return i + 1

        return N + 1


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 0], 3),
    pytest.param([3, 4, -1, 1], 2),
    pytest.param([7, 8, 9, 11, 12], 1),
])
def test_solutions(args, expected):
    assert Solution().firstMissingPositive(args) == expected
    assert Solution1().firstMissingPositive(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
