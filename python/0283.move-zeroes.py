#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 13:32:46
# @Last Modified : 2020-04-06 13:32:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:

    def moveZeroes0(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        start, end = 0, len(nums) - 1
        while True:
            while start < end and nums[start] != 0:
                start += 1
            while start < end and nums[end] == 0:
                end -= 1
            if start >= end:
                break
            cur_index = start
            while cur_index <= end - 1:
                nums[cur_index] = nums[cur_index + 1]
                cur_index += 1
            nums[cur_index] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNoZeroIdx = 0
        for idx, v in enumerate(nums):
            if v != 0:
                nums[lastNoZeroIdx] = nums[idx]
                lastNoZeroIdx += 1
        for i in range(lastNoZeroIdx,len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    sol = Solution()
    sample = [0, 1, 0, 3, 12]
    sample1 = [0, 1, 0, 3, 0, 120, 0]
    sample2 = [2, 0, 1, 0, 3, 0, 120, 0]
    sample3 = [0, 0]
    sample4 = [2, 1]
    print(sol.moveZeroes(sample))
    print(sol.moveZeroes(sample1))
    print(sol.moveZeroes(sample2))
    print(sol.moveZeroes(sample3))
    print(sol.moveZeroes(sample4))
    print(sample, sample1, sample2, sample3, sample4)
