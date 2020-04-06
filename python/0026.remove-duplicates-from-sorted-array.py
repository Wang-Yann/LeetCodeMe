#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 9:07 PM
# @Last Modified : 4/4/20 9:07 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
                length -= 1
            else:
                i += 1
        return length


if __name__ == '__main__':
    sol = Solution()
    sample = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sample1 = [1, 1, 2]
    print(sol.removeDuplicates(sample))
    print(sol.removeDuplicates(sample1))
    print(sample)
    print(sample1)
