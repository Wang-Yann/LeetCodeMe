#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  注意: 
# 
#  
#  每个数组中的元素不会超过 100 
#  数组的大小不会超过 200 
#  
# 
#  示例 1: 
# 
#  输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
#  
# 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        """0-1背包"""
        total = sum(nums)
        if total & 0b1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for v in range(target, num - 1, -1):
                dp[v] = dp[v] or dp[v - num]
        # print(dp)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def canPartition(self, nums: List[int]) -> bool:
        """
        状态定义：dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于 j
        1、不选择 nums[i]，如果在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i][j] = true；
        2、选择 nums[i]，如果在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]。
        """
        N = len(nums)
        total = sum(nums)
        target = total // 2
        if total & 0b1:
            return False
        dp = [[False] * (target + 1) for _ in range(N)]
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, N):
            for j in range(target + 1):
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                elif nums[i] < j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
        return dp[N - 1][target]


@pytest.mark.parametrize("args,expected", [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
])
def test_solutions(args, expected):
    assert Solution().canPartition(args) == expected
    assert Solution1().canPartition(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
