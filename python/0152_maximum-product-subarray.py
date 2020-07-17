#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 21:18:44
# @Last Modified : 2020-04-15 21:18:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
#  示例 1:
#
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#  Related Topics 数组 动态规划
#  👍 666 👎 0

"""

from functools import reduce
from typing import List

import pytest


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


class Solution1:

    def maxProduct(self, nums):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in nums:
            local_max = max(1, local_max)
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max


@pytest.mark.parametrize("args,expected", [
    ([2, 3, -2, 4], 6),
    ([-2, -3, -10000, 100, 0, -1], 3000000),
    ([-1, -2, -9, -6], 108),
    pytest.param([-2, 0, -1], 0),
])
def test_solutions(args, expected):
    assert Solution().maxProduct(args) == expected
    assert Solution1().maxProduct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
