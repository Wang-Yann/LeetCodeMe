#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。 
# 
#  示例 1: 
# 
#  
# 输入: [3, 2, 1]
# 
# 输出: 1
# 
# 解释: 第三大的数是 1.
#  
# 
#  示例 2: 
# 
#  
# 输入: [1, 2]
# 
# 输出: 2
# 
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
#  
# 
#  示例 3: 
# 
#  
# 输入: [2, 2, 3, 1]
# 
# 输出: 1
# 
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
#  
#  Related Topics 数组

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        for v in nums:
            if v in (first, second, third):
                continue
            if v > first:
                first, second, third = v, first, second
            elif third < v < second:
                third = v
            elif second < v < first:
                second, third = v, second
        if third == float("-inf"):
            return first
        return third


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([3, 2, 1], 1),
    pytest.param([1, 2], 2),
    pytest.param([2, 2, 3, 1], 1),
])
def test_solutions(args, expected):
    assert Solution().thirdMax(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
