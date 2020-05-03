#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:54:58
# @Last Modified : 2020-05-03 14:54:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
