#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 9:26 PM
# @Last Modified : 4/4/20 9:26 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


class Solution:
    def removeElement0(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums.remove(nums[i])
                length -= 1
            else:
                i+=1
        return length

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j =0
        while j < len(nums):
            if nums[j] != val:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i


if __name__ == '__main__':
    sol = Solution()
    sample = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sample1 = [1, 1, 2]
    print(sol.removeElement(sample, 3))
    print(sol.removeElement(sample1, 1))
    print(sample)
    print(sample1)
