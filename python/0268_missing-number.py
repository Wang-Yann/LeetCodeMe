#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 13:32:46
# @Last Modified : 2020-04-06 13:32:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums: return 0
        length = len(nums)
        return (length+1)*(length)//2-sum(nums)

    def missingNumberBit(self, nums: List[int]) -> int:
        length = len(nums)
        missing = length
        for i,v in enumerate(nums):
            missing ^= i^v
        return missing


if __name__ == '__main__':
    sol = Solution()
    sample=[9,6,4,2,3,5,7,0,1]
    print(sol.missingNumberBit(sample))
    print(sol.missingNumberBit([]))
