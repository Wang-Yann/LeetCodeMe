#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 15:40:08
# @Last Modified : 2020-04-22 15:40:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """me"""
        length = len(nums)
        if not length: return 0
        if length <= 2: return max(nums)
        dp1 = [0] * length
        dp2 = [0] * length
        dp1[0], dp2[1] = nums[0], nums[1]
        for i in range(1, length - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        for i in range(2, length):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[length - 2], dp2[length - 1])

class Solution1:
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.robRange(nums, 0, len(nums) - 1),
                   self.robRange(nums, 1, len(nums)))

    def robRange(self, nums, start, end):
        num_i, num_i_1 = nums[start], 0
        for i in range(start + 1, end):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(nums[i] + num_i_2, num_i_1)

        return num_i


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [2, 3],
        [4]

    ]
    lists = [x for x in samples]
    res = [sol.rob(x) for x in lists]
    print(res)
