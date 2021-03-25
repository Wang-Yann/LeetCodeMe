#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:40:50
# @Last Modified : 2020-04-30 17:40:50
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[
# l] = 0。
#
#  为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最
# 终结果不会超过 231 - 1 。
#
#  例如:
#
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#  Related Topics 哈希表 二分查找
#  👍 173 👎 0

"""

import collections
from typing import List

import pytest


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A_B_sum=collections.Counter(a+b for a in A for b in B)
        res = sum(A_B_sum[-c-d] for c in C for d in D)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(
        A=[1, 2],
        B=[-2, -1],
        C=[-1, 2],
        D=[0, 2]
    ), 2]
])
def test_solutions(kw, expected):
    assert Solution().fourSumCount(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
