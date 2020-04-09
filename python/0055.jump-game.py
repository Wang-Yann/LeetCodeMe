#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 22:47:01
# @Last Modified : 2020-04-08 22:47:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res_queue=[0]
        l = len(nums)
        while  res_queue:
            v = res_queue.pop()
            max_v = v+nums[v]
            if max_v>=l-1:
                return True
            for j in range(v+1,max_v+1):
                if nums[j] and nums[j]+j>max_v:
                    res_queue.append(j)
        return False

    def canJumpSimple(self, nums: List[int]) -> bool:
        lasPos = len(nums)-1
        for i in range(lasPos-1,-1,-1):
            if i +nums[i]>=lasPos:
                lasPos = i
        return lasPos==0






if __name__ == '__main__':
    sol = Solution()
    sample=[2,3,1,1,4]
    # sample=[8,2,4,4,4,9,5,2,5,8,8,0,0,0,3,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    sample=[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(sol.canJump(sample))
    print(sol.canJumpSimple(sample))
