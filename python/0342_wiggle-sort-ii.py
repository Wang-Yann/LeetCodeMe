#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 20:37:04
# @Last Modified : 2020-05-01 20:37:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        先将nums逆序排序，然后在中间将数组折断，间隔插入

        """
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]



@pytest.mark.parametrize("nums,expected", [
    ([1, 5, 1, 1, 6, 4], [1, 4, 1, 5, 1, 6]),
    pytest.param([1, 3, 2, 2, 3, 1], [2, 3, 1, 3, 1, 2]),
])
def test_solutions(nums, expected):
    Solution().wiggleSort(nums)
    i = 1
    while i < len(nums) - 1:
        if i % 2 == 0:
            assert nums[i - 1] > nums[i] < nums[i + 1]
        else:
            assert nums[i - 1] < nums[i] > nums[i + 1]
        i += 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
