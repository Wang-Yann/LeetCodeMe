#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 13:46:06
# @Last Modified : 2020-05-03 13:46:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 一个已排序好的表 A，其包含 1 和其他一些素数. 当列表中的每一个 p<q 时，我们可以构造一个分数 p/q 。
#
#  那么第 k 个最小的分数是多少呢? 以整数数组的形式返回你的答案, 这里 answer[0] = p 且 answer[1] = q.
#
#  示例:
# 输入: A = [1, 2, 3, 5], K = 3
# 输出: [2, 5]
# 解释:
# 已构造好的分数,排序后如下所示:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# 很明显第三个最小的分数是 2/5.
#
# 输入: A = [1, 7], K = 1
# 输出: [1, 7]
#
#
#  注意:
#
#
#  A 长度的取值范围在 2 — 2000.
#  每个 A[i] 的值在 1 —30000.
#  K 取值范围为 1 —A.length * (A.length - 1) / 2
#
#  Related Topics 堆 二分查找
#  👍 51 👎 0

"""

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
