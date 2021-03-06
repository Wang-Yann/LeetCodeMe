#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 22:40:42
# @Last Modified : 2020-04-10 22:40:42
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
#  示例 1:
#
#  输入: 123
# 输出: 321
#
#
#  示例 2:
#
#  输入: -123
# 输出: -321
#
#
#  示例 3:
#
#  输入: 120
# 输出: 21
#
#
#  注意:
#
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#  Related Topics 数学
#  👍 2029 👎 0

"""

import pytest


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag = -1 if x < 0 else 1
        x = flag * x
        INT_MAX = 2 ** 31 - 1
        INT_HEAD, MIN_LAST, MAX_LAST = INT_MAX // 10, 8, 7
        while x != 0:
            v = x % 10
            x = x // 10
            if num > INT_HEAD or (
                num == INT_HEAD and (flag == -1 and v > MIN_LAST or flag == 1 and v > MAX_LAST)
            ):
                return 0
            num = num * 10 + v

        return num * flag


class Solution1(object):
    def reverse(self, x):
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        # Handle overflow.
        return result if result <= 0x7fffffff else 0


@pytest.mark.parametrize("args,expected", [
    (-123, -321),
    (120, 21),
    (2 ** 31 + 1, 0),
    (2 ** 31 // 10, 463847412),
])
def test_solutions(args, expected):
    assert Solution().reverse(args) == expected
    assert Solution1().reverse(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
