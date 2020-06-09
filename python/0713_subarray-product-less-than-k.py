#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数数组 nums。 
# 
#  找出该数组内乘积小于 k 的连续的子数组的个数。 
# 
#  示例 1: 
# 
#  
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#  
# 
#  说明: 
# 
#  
#  0 < nums.length <= 50000 
#  0 < nums[i] < 1000 
#  0 <= k < 10^6 
#  
#  Related Topics 数组 双指针

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """滑动窗口"""
        if k <= 1:
            return 0
        ans, l, product = 0, 0, 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            ans += r - l + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[10, 5, 2, 6], k=100), 8],
    [dict(nums=[1, 1, 1], k=1), 0],
    [dict(nums=[1] * 100000, k=100), 5000050000],
])
def test_solutions(kw, expected):
    assert Solution().numSubarrayProductLessThanK(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
