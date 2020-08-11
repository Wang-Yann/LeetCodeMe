#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
#  现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  说明: 
# 
#  
#  你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。 
#  0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 
#  
# 
#  示例: 
# 
#  输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#  
#  Related Topics 分治算法 动态规划

"""

import functools
from typing import List

import pytest


class Solution1:
    """
    DP　自顶而下
     定义方法 dp，使其返回开区间 (left, right) 中所能得到的最大金币数。对于基础情况 (即 left + 1 == right)，这时候区间内没有整数，
     也没有气球需要加进去，因此 dp[left][right] = 0。随后在区间中加入气球，把问题分割成左右两部分来处理，找到最大金币数。

    在添加第 i 个气球后能得到的最大金币数为：
    nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)

    """

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0
            return max(
                nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
                for i in range(left + 1, right)
            )

        return dp(0, len(nums) - 1)


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # reframe problem as before
        nums = [1] + nums + [1]
        N = len(nums)

        # dp will store the results of our calls
        dp = [[0] * N for _ in range(N)]

        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(N - 2, -1, -1):
            for right in range(left + 2, N):
                # same formula to get the best score from (left, right) as before
                dp[left][right] = max(
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    for i in range(left + 1, right)
                )

        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([3, 1, 5, 8], 167)
])
def test_solutions(args, expected):
    assert Solution().maxCoins(args) == expected
    assert Solution1().maxCoins(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
