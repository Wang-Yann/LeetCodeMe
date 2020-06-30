#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M
#  的子数组之前或之后。） 
# 
#  从形式上看，返回最大的 V，而 V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... +
#  A[j+M-1]) 并满足下列条件之一： 
# 
#  
# 
#  
#  0 <= i < i + L - 1 < j < j + M - 1 < A.length, 或 
#  0 <= j < j + M - 1 < i < i + L - 1 < A.length. 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
#  
# 
#  示例 2： 
# 
#  输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# 输出：29
# 解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
#  
# 
#  示例 3： 
# 
#  输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。 
# 
#  
# 
#  提示： 
# 
#  
#  L >= 1 
#  M >= 1 
#  L + M <= A.length <= 1000 
#  0 <= A[i] <= 1000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
        GOOD Good Answer
        From LeetCode International
        https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/278251/JavaC%2B%2BPython-O(N)Time-O(1)-Space

        Lsum, sum of the last L elements
        Msum, sum of the last M elements

        Lmax, max sum of contiguous L elements before the last M elements.
        Mmax, max sum of contiguous M elements before the last L elements/
        """
        N = len(A)
        for i in range(1, N):
            A[i] += A[i - 1]
        res, L_max, M_max = A[L + M - 1], A[L - 1], A[M - 1]

        for i in range(L + M, N):
            # // 分别以L在前M在后，M在前L在后两种方式，滑动窗口，每次移动一格。

            L_max = max(L_max, A[i - M] - A[i - L - M])
            M_max = max(M_max, A[i - L] - A[i - L - M])
            res = max(res, L_max + A[i] - A[i - M], M_max + A[i] - A[i - L])
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2), 20],
    [dict(A=[3, 8, 1, 3, 2, 1, 8, 9, 0], L=3, M=2), 29],
    [dict(A=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3), 31],
])
def test_solutions(kw, expected):
    assert Solution().maxSumTwoNoOverlap(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
