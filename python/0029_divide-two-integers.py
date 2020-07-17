#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 13:42:09
# @Last Modified : 2020-04-29 13:42:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
#  返回被除数 dividend 除以除数 divisor 得到的商。
#
#  整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
#
#
#
#  示例 1:
#
#  输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
#
#  示例 2:
#
#  输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#
#
#
#  提示：
#
#
#  被除数和除数均为 32 位有符号整数。
#  除数不为 0。
#  假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
#
#  Related Topics 数学 二分查找
#  👍 380 👎 0

"""

import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648,res),2147483647)


@pytest.mark.parametrize("args", [
    (10, 3, 3),
    (7, -3, -2),

])
def test_solution(args):
    sol = Solution()
    *args, expected = args
    assert sol.divide(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
