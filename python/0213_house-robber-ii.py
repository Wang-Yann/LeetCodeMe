#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 15:40:08
# @Last Modified : 2020-04-22 15:40:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋
# 装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
#  给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
#  示例 1:
#
#  输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
#  示例 2:
#
#  输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
#  Related Topics 动态规划
#  👍 315 👎 0

"""

from typing import List

import pytest


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


@pytest.mark.parametrize("args,expected", [
    [[2, 3, 2], 3],
    [[1, 2, 3, 1], 4],
    [[2, 3], 3],
    [[4], 4],
])
def test_solutions(args, expected):
    assert Solution().rob(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
