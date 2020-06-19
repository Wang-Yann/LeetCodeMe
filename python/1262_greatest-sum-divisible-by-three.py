#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,6,5,1,8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。 
# 
#  示例 2： 
# 
#  输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,2,3,4,4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 4 * 10^4 
#  1 <= nums[i] <= 10^4 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for cur in [num + x for x in dp]:
                dp[cur % 3] = max(dp[cur % 3], cur)
        # print(dp)
        return dp[0]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        one, two = [], []
        nums.sort()
        sum_val = 0
        for v in nums:
            if v % 3 == 1:
                one.append(v)
            elif v % 3 == 2:
                two.append(v)
            sum_val += v
        ans = 0
        if sum_val % 3 == 0:
            return sum_val
        elif sum_val % 3 == 1:
            if len(two) >= 2:
                ans = max(ans, sum_val - two[0] - two[1])
            if len(one):
                ans = max(ans, sum_val - one[0])
        elif sum_val % 3 == 2:
            if len(two):
                ans = max(ans, sum_val - two[0])
            if len(one) >= 2:
                ans = max(ans, sum_val - one[0] - one[1])
        return ans


@pytest.mark.parametrize("args,expected", [
    ([3, 6, 5, 1, 8], 18),
    ([4], 0),
    ([1, 2, 3, 4, 4], 12),
])
def test_solutions(args, expected):
    assert Solution().maxSumDivThree(args) == expected
    assert Solution1().maxSumDivThree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
