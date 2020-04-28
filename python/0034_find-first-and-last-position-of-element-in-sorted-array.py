#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 17:41:24
# @Last Modified : 2020-04-06 17:41:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(lambda x, y:x >= y, nums, target)
        if left > len(nums)-1 or nums[left] != target:
            return [-1, -1]
        right = self.binarySearch(lambda x, y:x > y, nums, target)
        return [left, right - 1]

    def binarySearch(self, com_func, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if com_func(nums[mid], target):
                right = mid-1
            else:
                left =mid+1
        return left


if __name__ == '__main__':
    sol = Solution()
    sample = [4, 5, 6, 7, 0, 1, 2]
    sample = [ 0, 1, 2, 3,3, 4, 5]
    # sample = [ 1]
    print(sol.searchRange(sample, 1))
