#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 20:24:58
# @Last Modified : 2020-05-05 20:24:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）
#
#  返回true ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。
#
#
# 示例:
# 输入:
# [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
#
#
#  注意:
#
#
#  A 数组的长度范围为 [1, 30].
#  A[i] 的数据范围为 [0, 10000].
#
#  Related Topics 数学
#  👍 45 👎 0

"""

from typing import List

import pytest


class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        """
        HARD
        设 A0 中所有选择的方法得到的元素之和的集合为 left，A1 中所有选择的方法得到的元素之和的集合为 right，
        那么我们只需要在 left 中找出一个 x，使得 right 中包含 -x，那么就找到了一种和为 0 的方法。
        需要注意的是，我们不能同时选择 A0 和 A1 中的所有元素，这样 C 就为空了

        """
        from fractions import Fraction
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]
        # print(A )
        if N < 2:
            return False
        left = {A[0]}
        for i in range(1, N // 2):
            left = {z + A[i] for z in left} | left | {A[i]}
        # print("left | ",left)
        if 0 in left:
            return True
        right = {A[-1]}
        for i in range(N // 2, N - 1):
            right = {z + A[i] for z in right} | right | {A[i]}
        # print("right | ",right)
        if 0 in right:
            return True
        sum_left = sum(A[:N // 2])
        sum_right = sum(A[N // 2:])

        return any(-ha in right and (ha, -ha) != (sum_left, sum_right) for ha in left)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8], True),
    pytest.param([1], False),
])
def test_solutions(args, expected):
    assert Solution().splitArraySameAverage(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
