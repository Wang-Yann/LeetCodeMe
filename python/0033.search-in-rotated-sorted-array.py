#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 17:41:24
# @Last Modified : 2020-04-06 17:41:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+(right-right)//2
            if nums[mid]==target:
                return mid
            elif (nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right =mid-1
            else:
                left = mid+1
        return -1


if __name__ == '__main__':
    sol = Solution()
    sample = [4, 5, 6, 7, 0, 1, 2]
    sample = [ 7,9,0, 1, 2,3,4,5]
    print(sol.search(sample, 0))
