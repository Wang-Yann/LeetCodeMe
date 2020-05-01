#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 00:05:35
# @Last Modified : 2020-05-02 00:05:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
