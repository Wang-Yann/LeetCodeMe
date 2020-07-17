#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 15:40:08
# @Last Modified : 2020-04-22 15:40:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。
#
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
#  示例 1：
#
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
#
#  示例 2：
#
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 100
#  0 <= nums[i] <= 400
#
#  Related Topics 动态规划
#  👍 941 👎 0

"""

from typing import List

import pytest


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


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 3], 3),
    ([4], 4),
])
def test_solutions(args, expected):
    assert Solution().rob(args) == expected
    assert Solution().robS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
