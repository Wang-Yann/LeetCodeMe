#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。 
# 
#  让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组： 
# 
#  
#  A.length >= 3 
#  在 0 < i < A.length - 1 条件下，存在 i 使得：
#  
#  A[0] < A[1] < ... A[i-1] < A[i] 
#  A[i] > A[i+1] > ... > A[A.length - 1] 
#  
#  
#  
# 
#  
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：[3,5,5]
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：[0,3,2,1]
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  
# 
#  
# 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        l, r = 0, N - 1
        while l < N - 1 and A[l] < A[l + 1]:
            l += 1
        while r > 0 and A[r] < A[r - 1]:
            r -= 1
        return 0 < l < N - 1 and l == r


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):

    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1


@pytest.mark.parametrize("args,expected", [
    ([2, 1], False),
    ([3, 5, 5], False),
    ([0, 3, 2, 1], True),
])
def test_solutions(args, expected):
    assert Solution().validMountainArray(args) == expected
    assert Solution1().validMountainArray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
