#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 17:00:52
# @Last Modified : 2020-04-06 17:00:52
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = length - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def swap(self, nums: List[int], i: int, j: int) -> None:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums: List[int], start: int) -> None:
        left = start
        right = len(nums) - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 5, 4, 3, 3, 2]
    sample = [1, 8, 7, 3, 5, 6]
    sample = [3, 2, 1]
    sample = [3, 2, 1, 4, 5, 2]
    # sample=[1,2,3]
    print(sol.nextPermutation(sample))
    print(sample)
