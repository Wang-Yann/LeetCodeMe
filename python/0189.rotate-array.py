#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:53:32
# @Last Modified : 2020-04-06 12:53:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        length = len(nums)
        k = k % length
        for i in range(k):
            v = nums.pop()
            nums.insert(0, v)

    def rotateReverse(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(sol.rotateReverse(sample, 3))
    print(sample)
