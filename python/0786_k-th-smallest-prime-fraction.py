#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 13:46:06
# @Last Modified : 2020-05-03 13:46:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:

        """
        https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/solution/di-k-ge-zui-xiao-de-su-shu-fen-shu-by-leetcode/
        HARD........
        """
        from fractions import Fraction
        def under(x):
            """
            under(x) 用于求解小于 x 的分数数量
            返回小于 x 的分数数量以及小于 x 的最大分数
            使用二分查找找出一个 x，使得小于 x 的分数恰好有 K 个，并且记录其中最大的一个分数。

            """
            count = best = 0
            i = -1
            for j in range(1, len(A)):
                while A[i + 1] < A[j] * x:
                    i += 1
                count += i + 1
                if i >= 0:
                    best = max(best, Fraction(A[i], A[j]))
            return count, best

        lo, hi = 0.0, 1.0
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2.0
            count, best = under(mid)
            if count < K:
                lo = mid
            else:
                ans = best
                hi = mid

        return [ans.numerator, ans.denominator]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[1, 2, 3, 5], K=3), [2, 5]),
    pytest.param(dict(A=[1, 7], K=1), [1, 7]),
])
def test_solutions(kwargs, expected):
    assert Solution().kthSmallestPrimeFraction(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
