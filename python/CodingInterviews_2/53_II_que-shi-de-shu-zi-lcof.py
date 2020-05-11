#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出
# 这个数字。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1,3]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 10000 
#  Related Topics 数组 二分查找

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[m] == m:
                l = m + 1
            else:
                r = m - 1
        return l


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] != mid:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                r = mid - 1
            else:
                l = mid + 1
        if l == length:
            return length
        return -1


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 3], 2),
    pytest.param([0, 1, 2, 3, 4, 5, 6, 7, 9], 8),
])
def test_solutions(args, expected):
    assert Solution().missingNumber(args) == expected
    assert Solution1().missingNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
