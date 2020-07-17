#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:49:18
# @Last Modified : 2020-05-05 15:49:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
#
#  给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
#
#
#
#  示例：
#
#  输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
#
#
#
#
#  提示：
#
#  输入的数字 n 不会超过 100,000,000. (1e8)
#  Related Topics 数学
#  👍 67 👎 0

"""

import math

import pytest


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """注意审题"""
        if num <= 0: return False
        factor_sum = 0
        sqrt_val = math.floor(math.sqrt(num))
        for i in range(1, sqrt_val + 1):
            if num % i == 0:
                factor_sum += i
                if i * i != num:
                    factor_sum += num // i
        return factor_sum == 2 * num


class Solution1:
    def checkPerfectNumber(self, num: int) -> bool:
        """欧几里得-欧拉定理

        每个偶完全数都可以写成  2**(p-1)*(2**p-1)
        的形式，其中 p 为素数
        """

        def Pn(p):
            return (1 << (p - 1)) * ((1 << p) - 1)

        if num <= 0: return False
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            if Pn(prime) == num:
                return True
        return False


@pytest.mark.parametrize("args,expected", [
    (28, True),
    pytest.param(6, True),
    pytest.param(99999992, False),
])
def test_solutions(args, expected):
    assert Solution().checkPerfectNumber(args) == expected
    assert Solution1().checkPerfectNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
