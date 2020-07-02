#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个正整数的数组 A（其中的元素不一定完全不同），请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的
# 最大可能排列。 
# 
#  如果无法这么操作，就请返回原数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[3,2,1]
# 输出：[3,1,2]
# 解释：
# 交换 2 和 1
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：[1,1,5]
# 输出：[1,1,5]
# 解释： 
# 这已经是最小排列
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：[1,9,4,6,7]
# 输出：[1,7,4,6,9]
# 解释：
# 交换 9 和 7
#  
# 
#  
# 
#  示例 4： 
# 
#  输入：[3,1,1,3]
# 输出：[1,3,1,3]
# 解释：
# 交换 1 和 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= A[i] <= 10000 
#  
#  Related Topics 贪心算法 数组

"""
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        """
        Test cases was wrong
        寻找在 A[i] 最左边且小于 A[i] 的最大的数字 A[j]
        Go from right side to left until numbers are getting smaller.
        Go from left side to right until the number is both higher than previous and smaller than the number on the leftmost side.
        Swap leftmost with the one from (2) and return.

        """
        left = len(A) - 1
        while left - 1 >= 0 and A[left - 1] <= A[left]:
            left -= 1
        if left == 0:
            return A
        right = left
        for i in range(left, len(A)):
            if A[left - 1] > A[i] > A[right]:
                right = i
        A[right], A[left - 1] = A[left - 1], A[right]
        return A


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def prevPermOpt1(self, A):
        for left in reversed(range(len(A) - 1)):
            if A[left] > A[left + 1]:
                break
        else:
            return A
        right = len(A) - 1
        while A[left] <= A[right]:
            right -= 1
        while A[right - 1] == A[right]:
            right -= 1
        A[left], A[right] = A[right], A[left]
        return A


@pytest.mark.parametrize("args,expected", [
    ([3, 2, 1], [3, 1, 2]),
    ([1, 1, 5], [1, 1, 5]),
    ([1, 9, 4, 6, 7], [1, 7, 4, 6, 9]),
    ([3, 1, 1, 3], [1, 3, 1, 3]),
])
def test_solutions(args, expected):
    args1 = copy.deepcopy(args)
    assert Solution().prevPermOpt1(args) == expected
    assert Solution1().prevPermOpt1(args1) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
