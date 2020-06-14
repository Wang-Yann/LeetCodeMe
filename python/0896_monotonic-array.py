#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果数组是单调递增或单调递减的，那么它是单调的。 
# 
#  如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是
# 单调递减的。 
# 
#  当给定的数组 A 是单调数组时返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[1,2,2,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：[6,5,4,4]
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：[1,3,2]
# 输出：false
#  
# 
#  示例 4： 
# 
#  输入：[1,2,4,5]
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：[1,1,1]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 50000 
#  -100000 <= A[i] <= 100000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        same = [A[i] - A[i - 1] for i in range(1, len(A))]
        return not same or all(x >= 0 for x in same) or all(x <= 0 for x in same)


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def isMonotonic(self, A):
        inc, dec = False, False
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                inc = True
            elif A[i] > A[i+1]:
                dec = True
        return not inc or not dec

@pytest.mark.parametrize("args,expected", [
    ([1, 2, 2, 3], True),
    ([6, 5, 4, 4], True),
    ([1, 3, 2], False),
    ([1, 2, 4, 5], True),
    ([1], True),
    pytest.param([1, 1, 1], True),
])
def test_solutions(args, expected):
    assert Solution().isMonotonic(args) == expected
    assert Solution1().isMonotonic(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
