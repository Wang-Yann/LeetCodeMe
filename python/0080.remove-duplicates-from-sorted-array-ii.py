#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 22:19:00
# @Last Modified : 2020-04-12 22:19:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if not length: return 0
        last,i,is_same = 0,1,False
        while i <length:
            if nums[last]!=nums[i] or not is_same:
                is_same  = nums[last]==nums[i]
                last+=1
                nums[last]=nums[i]
            i+=1
        return last+1

    def removeDuplicatesMe(self, nums: List[int]) -> int:
        length = len(nums)
        if length<=2:return  length
        pos_cur =1
        l=1
        cnt = 1
        while l<=length-1:
            if nums[l]==nums[l-1]:
                cnt+=1
            else:
                cnt=1
            if cnt<=2:
                nums[pos_cur] = nums[l]
                pos_cur+=1
            l+=1
        return pos_cur




if __name__ == '__main__':
    sol = Solution()
    samples=[
        [1,1,1,2,2,3],
        [0,0,1,1,1,1,2,3,3],
        [-1,1,1,1,1,2,3,3],
        [1,1,1,2,2,3],
        [1,2,2]
    ]
    res = [ sol.removeDuplicates(x) for x in samples]
    # res = [ sol.removeDuplicatesMe(x) for x in samples]
    print(res)
    print(samples)