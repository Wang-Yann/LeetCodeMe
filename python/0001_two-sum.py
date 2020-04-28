#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 2:
            return []
        for i in range(0, length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 9, 11, 15], 18))
    print(sol.twoSum([3, 2, 4], 6))
