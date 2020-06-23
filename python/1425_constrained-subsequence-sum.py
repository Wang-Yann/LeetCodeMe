#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 num
# s[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。 
# 
#  数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [10,2,-10,5,20], k = 2
# 输出：37
# 解释：子序列为 [10, 2, 5, 20] 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [-1,-2,-3], k = 1
# 输出：-1
# 解释：子序列必须是非空的，所以我们选择最大的数字。
#  
# 
#  示例 3： 
# 
#  输入：nums = [10,-2,-10,-5,20], k = 2
# 输出：23
# 解释：子序列为 [10, -2, -5, 20] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  
#  Related Topics 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        定义状态dp[i]为以i结尾的的最大子序和
        那么当考虑第i+1个的时候，由于相邻两个下标差距不大于k且非空，所以有以下状态转移方程
            dp[i+1] = max(nums[i+1], dp[i+1-j] + nums[i+1])
        (1 <= j <= k )
        """
        N = len(nums)
        dp = nums[:]
        s = collections.deque([(nums[0], 0)])
        for i in range(1, N):
            dp[i] = max(dp[i], s[0][0] + nums[i])
            while s and s[-1][0] <= dp[i]:
                s.pop()
            s.append((dp[i], i))
            if i - s[0][1] >= k:
                s.popleft()
        # print(dp)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[10, 2, -10, 5, 20], k=2), 37],
    [dict(nums=[-1, -2, -3], k=1), -1],
    [dict(nums=[10, -2, -10, -5, 20], k=2), 23],
])
def test_solutions(kw, expected):
    assert Solution().constrainedSubsetSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
