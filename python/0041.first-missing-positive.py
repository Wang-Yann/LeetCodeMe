#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-07 21:13:53
# @Last Modified : 2020-04-07 21:13:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

"""
https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        i=0
        # 3 应该放在索引为 2 的地方
        # 4 应该放在索引为 3 的地方

        while i<=len(nums) -1:
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            if nums[i]> 0 and nums[i]-1<length and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i] ,nums[nums[i]-1]
            else:
                i+=1
        print(nums)
        for i, integer in enumerate(nums):
            if integer != i + 1:
                return i + 1
        return  length + 1




if __name__ == '__main__':
    sol = Solution()
    sample=[3,4,-1,1]
    print(sol.firstMissingPositive(sample))
