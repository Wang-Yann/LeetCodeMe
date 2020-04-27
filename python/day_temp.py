#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 15:00:24
# @Last Modified : 2020-04-27 15:00:24
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# search-in-rotated-sorted-array
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif (nums[l] <= target < nums[mid]) or (
                    nums[mid] < nums[l] and not nums[mid] < target <= nums[r]):
                r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(nums=[4, 5, 6, 7, 0, 1, 2], target=0),
        dict(nums=[4, 5, 6, 7, 0, 1, 2], target=3)

    ]
    lists = [x for x in samples]
    res = [sol.search(**x) for x in lists]
    print(res)
