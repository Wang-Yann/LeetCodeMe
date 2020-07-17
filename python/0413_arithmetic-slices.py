#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:01:17
# @Last Modified : 2020-05-05 15:01:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
#
#  例如，以下数列为等差数列:
#
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
#  以下数列不是等差数列。
#
#
# 1, 1, 2, 5, 7
#
#
#
#  数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
#
#  如果满足以下条件，则称子数组(P, Q)为等差数组：
#
#  元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。
#
#  函数要返回数组 A 中所有为等差数组的子数组个数。
#
#
#
#  示例:
#
#
# A = [1, 2, 3, 4]
#
# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
#
#  Related Topics 数学 动态规划
#  👍 147 👎 0

"""

from typing import List

import pytest


class Solution:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans, i = 0, 0
        length = len(A)
        while i < length - 2:
            start = i
            while i < length - 2 and A[i + 2] + A[i] == 2 * A[i + 1]:
                ans += i - start + 1
                i += 1
            i += 1
        return ans


class Solution1:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """DP
        dp[i] 用来存储在区间 (k,i)， 而不在区间 (k,j)中等差数列的个数，
        """
        length = len(A)
        dp = [0] * length
        # ans=0
        for i in range(2, length):
            if A[i - 2] + A[i] == 2 * A[i - 1]:
                dp[i] = dp[i - 1] + 1
                # ans+=dp[i]
        print(dp)
        return sum(dp)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4], 3),
    ([7, 7, 7, 7], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8], 21),
    ([1, 3, 5, 7, 9, 15, 20, 25, 28], 7)
])
def test_solutions(args, expected):
    assert Solution().numberOfArithmeticSlices(args) == expected
    assert Solution1().numberOfArithmeticSlices(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
