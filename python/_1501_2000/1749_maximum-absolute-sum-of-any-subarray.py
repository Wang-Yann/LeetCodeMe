#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 16:54:54
# @Last Modified : 2021-02-27 16:54:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 。一个子数组 [numsl, numsl+1, ..., numsr-1, numsr] 的 和的绝对值 为 abs(numsl
#  + numsl+1 + ... + numsr-1 + numsr) 。 
# 
#  请你找出 nums 中 和的绝对值 最大的任意子数组（可能为空），并返回该 最大值 。 
# 
#  abs(x) 定义如下： 
# 
#  
#  如果 x 是负整数，那么 abs(x) = -x 。 
#  如果 x 是非负整数，那么 abs(x) = x 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-3,2,3,-4]
# 输出：5
# 解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,-5,1,-4,3,-2]
# 输出：8
# 解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics 贪心算法 
#  👍 5 👎 0
  

"""
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        itertools.accumulate
        tertools.accumulate(nums, initial=0)
        Changed in version 3.8: Added the optional initial parameter.
        ---
        https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/discuss/1052527/JavaC%2B%2BPython-O(1)-Space
        abs subarray sum
        = one prefix sum - the other prefix sum
        <= maximum prefix sum - minimum prefix sum

        """
        return max(itertools.accumulate([0] + nums)) - min(itertools.accumulate([0] + nums))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, -3, 2, 3, -4]), 5],
    [dict(nums=[2, -5, 1, -4, 3, -2]), 8],
    [dict(nums=[-7, -1, 0, -2, 1, 3, 8, -2, -6, -1, -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]), 44],
    [dict(nums=[-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8]), 27],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maxAbsoluteSum(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
