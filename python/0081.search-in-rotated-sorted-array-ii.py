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
                return True
            elif (nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right =mid-1
            else:
                left = mid+1
        return False


if __name__ == '__main__':
    sol = Solution()
    sample = [2,5,6,0,0,1,2]
    sample1 = [2,5,6,0,0,1,2]
    print(sol.search(sample, 0))
    print(sol.search(sample1, 3))
