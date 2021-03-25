#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 13:53:26
# @Last Modified : 2020-04-29 13:53:26
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
#  Related Topics 数学 二分查找
#  👍 443 👎 0

"""

import pytest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)
        positive = 1 if n > 0 else -1
        res = 1
        while abs_n:
            if abs_n & 0b1:
                res *= x
            abs_n >>= 1
            x *= x
        if positive == -1:
            res = 1.0 / res
        return min(max(-2147483648, res), 2147483647)

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)



@pytest.mark.parametrize("args", [
    (2.0, 10, 1024.0),
    (2.10, 3, 9.2610),
    (2.0, -2, 0.25)
])
def test_solutions(args):
    *args, expected = args
    assert Solution().myPow(*args) == pytest.approx(expected, 0.001)
    assert Solution1().myPow(*args) == pytest.approx(expected, 0.001)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
