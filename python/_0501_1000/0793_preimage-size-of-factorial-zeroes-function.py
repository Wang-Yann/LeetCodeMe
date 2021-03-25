#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:00:19
# @Last Modified : 2020-05-03 14:00:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# f(x) 是 x! 末尾是0的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且0! = 1）
#
#  例如， f(3) = 0 ，因为3! = 6的末尾没有0；而 f(11) = 2 ，因为11!= 39916800末端有2个0。给定 K，找出多少个非负整
# 数x ，有 f(x) = K 的性质。
#
#
# 示例 1:
# 输入:K = 0
# 输出:5
# 解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。
#
# 示例 2:
# 输入:K = 5
# 输出:0
# 解释:没有匹配到这样的 x!，符合K = 5 的条件。
#
#
#  注意：
#
#
#
#  K是范围在 [0, 10^9] 的整数。
#
#
#  Related Topics 二分查找
#  👍 44 👎 0

"""


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
