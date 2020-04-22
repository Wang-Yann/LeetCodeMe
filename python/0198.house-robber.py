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
        length = len(nums)
        if not length: return 0
        dp = [0] * (length + 1)
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[length - 1]

    def robS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for v in nums:
            last, now = now, max(last + v, now)
        return now


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2, 3],
        [4]

    ]
    lists = [x for x in samples]
    res = [sol.rob(x) for x in lists]
    print(res)
