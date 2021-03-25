#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 03:39:44
# @Last Modified : 2021-02-24 03:39:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。 
# 
#  一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。 
# 
#  请你返回乘积为正数的最长子数组长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,-2,-3,4]
# 输出：4
# 解释：数组本身乘积就是正数，值为 24 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [0,1,-2,-3,-4]
# 输出：3
# 解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
# 注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。 
# 
#  示例 3： 
# 
#  输入：nums = [-1,-2,-3,0,1]
# 输出：2
# 解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
#  
# 
#  示例 4： 
# 
#  输入：nums = [-1,2]
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：nums = [1,2,3,5,-6,4,0,10]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^9 <= nums[i] <= 10^9 
#  
#  Related Topics 贪心算法 
#  👍 29 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        "pos[i]", "neg[i]" represent longest consecutive numbers ending with nums[i] forming a positive/negative product.
        """
        N = len(nums)
        pos, neg = [0] * N, [0] * N
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        ans = pos[0]
        for i in range(1, N):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, -2, -3, 4]), 4],
    [dict(nums=[0, 1, -2, -3, -4]), 3],
    [dict(nums=[-1, -2, -3, 0, 1]), 2],
    [dict(nums=[-1, 2]), 1],
    [dict(nums=[1, 2, 3, 5, -6, 4, 0, 10]), 4],
])
def test_solutions(kw, expected):
    assert Solution().getMaxLen(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
