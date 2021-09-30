#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 
#  
# 
#  示例 2: 
# 
#  输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
#  
# 
#  
# 
#  注意：数组长度不会超过10000。 
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 3, 5, 4, 7], 3),
    ([2, 2, 2, 2, 2], 1),
    ([], 0)
])
def test_solutions(args, expected):
    assert Solution().findLengthOfLCIS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])