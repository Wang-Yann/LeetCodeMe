#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 10:58:43
# @Last Modified : 2020-08-04 10:58:43
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定已经按升序排列、由不同整数组成的数组 A，返回满足 A[i] == i 的最小索引 i。如果不存在这样的 i，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[-10,-5,0,3,7]
# 输出：3
# 解释：
# 对于给定的数组，A[0] = -10，A[1] = -5，A[2] = 0，A[3] = 3，因此输出为 3 。
#  
# 
#  示例 2： 
# 
#  输入：[0,2,5,8,17]
# 输出：0
# 示例：
# A[0] = 0，因此输出为 0 。
#  
# 
#  示例 3： 
# 
#  输入：[-10,-5,3,4,7,9]
# 输出：-1
# 解释： 
# 不存在这样的 i 满足 A[i] = i，因此输出为 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length < 10^4 
#  -10^9 <= A[i] <= 10^9 
#  
#  Related Topics 数组 二分查找 
#  👍 15 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) >> 1
            if A[mid] < mid:
                l = mid + 1
            else:
                r = mid
        return l if A[l] == l else -1


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) >> 1
            if A[mid] >= mid:
                r = mid - 1
            else:
                l = mid + 1
        return l if l < len(A) and A[l] == l else -1


@pytest.mark.parametrize("args,expected", [
    ([-10, -5, 0, 3, 7], 3),
    ([0, 2, 5, 8, 17], 0),
    ([-10, -5, 3, 4, 7, 9], -1),
    ([-10], -1),
    ([-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10], 4),
])
def test_solutions(args, expected):
    assert Solution().fixedPoint(args) == expected
    assert Solution1().fixedPoint(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
