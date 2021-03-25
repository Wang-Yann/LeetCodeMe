#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。 
# 

"""

import functools
import operator
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        return functools.reduce(operator.xor, nums)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
    pytest.param([3, 3, 7, 7, 10, 11, 11], 10),
])
def test_solutions(args, expected):
    assert Solution().singleNonDuplicate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
