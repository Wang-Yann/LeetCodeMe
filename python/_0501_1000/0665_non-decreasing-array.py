#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。 
# 
#  我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#  
# 
#  
# 
#  说明： 
# 
#  
#  1 <= n <= 10 ^ 4 
#  - 10 ^ 5 <= nums[i] <= 10 ^ 5 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        """
        从头开始模拟，碰到第一次nums[i]<nums[i-1]时，我们需要修改nums[i]或者nums[i-1]来保证数组的不下降。
        有两种情况：
         1、nums[i]<nums[i-2]，比如3,4,2这样的情况，当前nums[i]=2。此时我们只能将nums[i]修改为4，才能在满足题意的条件下保证数组不下降，修改后为3,4,4。
         2、nums[i]>=nums[i-2]，比如3,5,4，当前nums[i]=4。此时我们可以将nums[i-1]修改为4，修改后为3,4,4
        """
        count = 0
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                count += 1
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return count <= 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([4, 2, 3], True),
    ([3, 4, 2, 3], False),
    pytest.param([4, 2, 1], False),
])
def test_solutions(args, expected):
    assert Solution().checkPossibility(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
