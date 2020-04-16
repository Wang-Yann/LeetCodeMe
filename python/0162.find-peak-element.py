#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 20:32:03
# @Last Modified : 2020-04-16 20:32:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                r = mid
            else:
                l=mid+1
        return l

if __name__ == '__main__':
    sol = Solution()
    samples=[
        [1,2,3,1],
        [1,2,1,3,5,6,4]
    ]
    res = [ sol.findPeakElement(x) for x in samples]
    print(res)


