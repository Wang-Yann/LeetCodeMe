#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 21:18:44
# @Last Modified : 2020-04-15 21:18:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from functools import reduce
from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        """
        f(i) = max(f(i-1)*nums[i],nums(i))
        """
        if not nums:
            return 0
        dp = [float("-inf")] * len(nums)
        dp_min = [float("inf")] * len(nums)
        dp_min[0] = dp[0] = nums[0]
        for i in range(1, len(nums)):
            v = nums[i]
            dp[i] = max(dp[i - 1] * v, dp_min[i - 1] * v, v)
            dp_min[i] = min(dp_min[i - 1] * v, dp[i - 1] * v, v)
        return reduce(max, dp)

    def maxProductS(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max = max(1, local_max)
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 3, -2, 4],
        [-2, 0, -1],
        [-2, -3, -10000, 100, 0, -1],
        [-1, -2, -9, -6]
    ]
    res = [sol.maxProduct(x) for x in samples]
    print(res)
