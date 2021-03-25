#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 nums ，你可以对它进行一些操作。 
# 
#  每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] +
#  1 的元素。 
# 
#  开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。 
# 
#  示例 1: 
# 
#  
# 输入: nums = [3, 4, 2]
# 输出: 6
# 解释: 
# 删除 4 来获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [2, 2, 3, 3, 3, 4]
# 输出: 9
# 解释: 
# 删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#  
# 
#  注意: 
# 
#  
#  nums的长度最大为20000。 
#  每个整数nums[i]的大小都在[1, 10000]范围内。 
#  
#  Related Topics 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        https://www.jiuzhang.com/problem/delete-and-earn/#tag-highlight-lang-python
        DP(i)表示删除的数字不超过i时所能获得的最大的分数。
        考虑当前数字是主动删的还是被动删的。 由于i-1和i+1是相互的，我们只考虑一边，避免重复
        """
        if not nums:
            return 0
        counter = collections.Counter(nums)
        dp = [0 for _ in range(10001)]
        dp[1] = counter[1]
        for i in range(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * counter[i])
        # print(dp)
        return dp[10000]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
])
def test_solutions(args, expected):
    assert Solution().deleteAndEarn(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
