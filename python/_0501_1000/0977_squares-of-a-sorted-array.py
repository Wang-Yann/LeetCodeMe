#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#  
# 
#  示例 2： 
# 
#  输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A 已按非递减顺序排序。 
#  
#  Related Topics 数组 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def sortedSquares(self, A: List[int]) -> List[int]:
        """利用已经排序条件"""
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        # print(i,j)
        ans = []
        while 0 <= i and j < N:
            if A[i] ** 2 < A[j] ** 2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1

        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
        while j < N:
            ans.append(A[j] ** 2)
            j += 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return [x ** 2 for x in sorted(A, key=abs)]


@pytest.mark.parametrize("args,expected", [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([-1], [1]),
    ([-1, 2, 2], [1, 4, 4]),
])
def test_solutions(args, expected):
    assert Solution().sortedSquares(args) == expected
    assert Solution1().sortedSquares(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
