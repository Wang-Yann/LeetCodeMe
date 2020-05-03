#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:00:19
# @Last Modified : 2020-05-03 14:00:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def preimageSizeFZF(self, K: int) -> int:
        """令 zeta(x) 为 x! 末尾零的个数。如果 x! 可以分解为素数的乘积，
            ，那么 x! 末尾零的个数为 min(a, b) = b。

            zeta(x) 就是 x 除以 5 的次数之和

            """

        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        lo, hi = K, 10 * K + 1
        while lo < hi:
            mid = (lo + hi) // 2
            zmid = zeta(mid)
            if zmid == K:
                return 5
            elif zmid < K:
                lo = mid + 1
            else:
                hi = mid - 1
        return 0


class Solution1:
    """https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/solution/shu-xue-tui-dao-by-jriver/
        Ci=5*C(i-1) + 1   C0 =0
        Ci=(5**i-1)/4
    """

    def preimageSizeFZF(self, K: int) -> int:
        step = 0
        while step < K:
            step = step * 5 + 1
        while K:
            step = (step - 1) // 5
            if K // step == 5:
                return 0
            K %= step
        return 5


@pytest.mark.parametrize("args,expected", [
    (0, 5),
    pytest.param(5, 0),
])
def test_solutions(args, expected):
    assert Solution().preimageSizeFZF(args) == expected
    assert Solution1().preimageSizeFZF(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
