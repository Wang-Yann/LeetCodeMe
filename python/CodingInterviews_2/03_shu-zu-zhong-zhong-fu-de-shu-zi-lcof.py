#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:13:31
# @Last Modified : 2020-04-22 23:13:31
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for v in nums:
            if v in hash_set:
                return v
            hash_set.add(v)

class Solution1:

    def findRepeatNumber(self, nums: List[int]) -> int:
        length =  len(nums)
        if not length:
            return None
        for i in range(length):
            if not 0<=nums[i]<=length-1:return None
            while i!=nums[i]:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                v=nums[i]
                nums[i],nums[v]  = nums[v],nums[i]



if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 3, 1, 0, 2, 5, 3]

    ]
    res = [sol.findRepeatNumber(x) for x in samples]
    print(res)
