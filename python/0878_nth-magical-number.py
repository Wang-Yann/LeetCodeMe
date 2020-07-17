#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:54:58
# @Last Modified : 2020-05-03 14:54:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 如果正整数可以被 A 或 B 整除，那么它是神奇的。
#
#  返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。
#
#
#
#
#
#
#  示例 1：
#
#  输入：N = 1, A = 2, B = 3
# 输出：2
#
#
#  示例 2：
#
#  输入：N = 4, A = 2, B = 3
# 输出：6
#
#
#  示例 3：
#
#  输入：N = 5, A = 2, B = 4
# 输出：10
#
#
#  示例 4：
#
#  输入：N = 3, A = 6, B = 4
# 输出：8
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#  2 <= A <= 40000
#  2 <= B <= 40000
#
#  Related Topics 数学 二分查找
#  👍 48 👎 0

"""

import pytest


class Solution:

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def check(lcm, target):
            return target // A + target // B - target // lcm >= N

        lcm = A * B // gcd(A, B)
        l, r = 0, max(A, B) * N
        while l <= r:
            mid = (l + r) >> 1
            if check(lcm, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l % (10 ** 9 + 7)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(N=1, A=2, B=3), 2),
    (dict(N=4, A=2, B=3), 6),
    (dict(N=5, A=2, B=4), 10),
    (dict(N=3, A=6, B=4), 8),
])
def test_solutions(kwargs, expected):
    assert Solution().nthMagicalNumber(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
