#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 13:32:46
# @Last Modified : 2020-04-06 13:32:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针
#  👍 653 👎 0

"""
import copy
from typing import List

import pytest


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        N = len(nums)
        left = right = 0
        while right < N:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


class Solution1:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoZeroIdx = 0
        for idx, v in enumerate(nums):
            if v != 0:
                nums[lastNoZeroIdx] = nums[idx]
                lastNoZeroIdx += 1
        for i in range(lastNoZeroIdx, len(nums)):
            nums[i] = 0


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
])
def test_solutions(args, expected):
    args1 = copy.deepcopy(args)
    Solution().moveZeroes(args)
    Solution1().moveZeroes(args1)
    assert args == expected
    assert args1 == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
