#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 22:17:36
# @Last Modified : 2020-04-16 22:17:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow = nums[0]
        fast = nums[nums[0]]


        while  slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # print(slow,fast)
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicateBin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            # Get count of num <= mid.
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    sol = Solution()
    samples=[
        [1,3,4,2,2],
        [3,1,3,4,2],
        [3,4,5,4,2,1]
    ]
    res = [ sol.findDuplicate(x) for x in samples]
    print(res)
