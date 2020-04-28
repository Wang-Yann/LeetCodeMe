#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 16:16:39
# @Last Modified : 2020-04-12 16:16:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        三向切分
        """
        length = len(nums)
        lo,hi = 0,length-1
        lt,gt=lo,hi
        i =lo
        MID_V=1
        while  i<=gt:
            if nums[i]<MID_V:
                nums[i],nums[lt]=nums[lt],nums[i]
                lt+=1
                i+=1
            elif nums[i]>MID_V:
                nums[i],nums[gt]=nums[gt],nums[i]
                gt-=1
            else:
                i+=1





if __name__ == '__main__':
    sol = Solution()
    samples=[
        [2,0,2,1,1,0],
        [0,0,2,0],
        [1,0,1,0]
    ]
    res = [ sol.sortColors(x) for x in samples]
    print(samples)