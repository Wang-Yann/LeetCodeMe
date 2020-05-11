#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        def helper(comp_func, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) >> 1
                if comp_func(nums[mid], target):
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        left = helper(lambda x, y:x >= y, target)
        if left > len(nums) - 1 or nums[left] != target:
            return 0
        right = helper(lambda x, y:x > y, target)
        return right - left


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[5, 7, 7, 8, 8, 10], target=8), 2),
    pytest.param(dict(nums=[5, 7, 7, 8, 8, 10], target=6), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().search(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
