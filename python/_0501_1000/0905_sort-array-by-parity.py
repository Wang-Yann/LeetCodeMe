#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。 
# 
#  你可以返回满足此条件的任何数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 5000 
#  0 <= A[i] <= 5000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        for v in A:
            if v % 2 == 0:
                ans.insert(0, v)
            else:
                ans.append(v)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):

    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A



@pytest.mark.parametrize("args,expected", [
    ([3, 1, 2, 4], [[4, 2, 3, 1], [2, 4, 1, 3], [4, 2, 1, 3], [2, 4, 3, 1]]),
])
def test_solutions(args, expected):
    assert Solution().sortArrayByParity(args) in expected
    assert Solution1().sortArrayByParity(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
