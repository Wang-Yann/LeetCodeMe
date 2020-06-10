#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个给定的数组nums中，总是存在一个最大元素 。 
# 
#  查找数组中的最大元素是否至少是数组中每个其他数字的两倍。 
# 
#  如果是，则返回最大元素的索引，否则返回-1。 
# 
#  示例 1: 
# 
#  输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.
#  
# 
#  
# 
#  提示: 
# 
#  
#  nums 的长度范围在[1, 50]. 
#  每个 nums[i] 的整数范围在 [0, 100]. 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        if any(x * 2 > max_val for x in nums if x != max_val):
            return -1
        return nums.index(max_val)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([3, 6, 1, 0], 1),
    ([1, 2, 3, 4], -1)
])
def test_solutions(args, expected):
    assert Solution().dominantIndex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
