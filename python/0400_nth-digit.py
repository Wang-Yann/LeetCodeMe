#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:51:01
# @Last Modified : 2020-05-05 14:51:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
#  注意:
# n 是正数且在32位整数范围内 ( n < 231)。
#
#  示例 1:
#
#  输入:
# 3
#
# 输出:
# 3
#
#
#  示例 2:
#
#  输入:
# 11
#
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
#
#  Related Topics 数学
#  👍 113 👎 0

"""
import pytest


class Solution:

    def findNthDigit(self, n: int) -> int:
        """https://leetcode-cn.com/problems/nth-digit/solution/xiang-jie-zhao-gui-lu-by-z1m/"""
        n -= 1
        for digits in range(1, 11):
            first_num = 10 ** (digits - 1)
            if n < 9 * first_num * digits:
                res_num = str(first_num + n // digits)
                return int(res_num[n % digits])
            n -= 9 * first_num * digits


class Solution1:

    def findNthDigit(self, n: int) -> int:
        num = 9
        digit = 1
        n-=1
        while n - num * digit > 0:
            n -= num * digit
            num *= 10
            digit += 1
        a, b = divmod(n, digit)
        return int(str(10 ** (digit - 1) + a)[b])


@pytest.mark.parametrize("args,expected", [
    (3, 3),
    pytest.param(11, 0),
])
def test_solutions(args, expected):
    assert Solution().findNthDigit(args) == expected
    assert Solution1().findNthDigit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
