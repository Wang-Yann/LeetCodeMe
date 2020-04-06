#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 9:43 PM
# @Last Modified : 4/4/20 9:43 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


class Solution:
    def searchInsert0(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return 1 if target > nums[0] else 0
        i = 0
        j = 1
        while j < length:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[i] < target:
                if nums[j] < target:
                    i += 1
                    j += 1
                else:
                    return j
            else:
                return i
        return j

    def binarysearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def binarysearchRec(self, nums, target) :
        return self.binarysearchRecurse(nums,target,0,len(nums)-1)

    def binarysearchRecurse(self, nums, target,low, high) :
        if low>high: return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarysearchRecurse(nums,target,mid+1,high)
        else:
            return self.binarysearchRecurse(nums,target,low,mid-1)


    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low = 0
        high = length - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    sol = Solution()
    sample = [0, 1, 2, 3, 13, 14]
    # print(sol.binarysearch(sample, 3))
    # print(sol.binarysearch(sample, 12))
    print(sol.searchInsert(sample, 3))
    print(sol.searchInsert(sample, -1))
    print(sol.searchInsert(sample, 15))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.binarysearchRec([1, 3, 5, 6], 3))
