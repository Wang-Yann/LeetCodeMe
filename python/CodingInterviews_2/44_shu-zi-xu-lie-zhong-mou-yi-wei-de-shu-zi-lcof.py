#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:13:45
# @Last Modified : 2020-05-10 18:13:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，
# 等等。
#
#  请写一个函数，求任意第n位对应的数字。
#
#
#
#  示例 1：
#
#  输入：n = 3
# 输出：3
#
#
#  示例 2：
#
#  输入：n = 11
# 输出：0
#
#
#
#  限制：
#
#
#  0 <= n < 2^31
#
#
#  注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
#  Related Topics 数学
#  👍 43 👎 0




import pytest


class Solution:

    def findNthDigit(self, n: int) -> int:
        num = 9
        digit = 1
        n -= 1
        while n - num * digit > 0:
            n -= num * digit
            num *= 10
            digit += 1
        times, rest = divmod(n, digit)
        # print("times,rest| digit,num", times, rest, digit, num)
        return int(str(10 ** (digit - 1) + times)[rest])


@pytest.mark.parametrize("args,expected", [
    # (3, 3),
    (1013, 7),
    # pytest.param(11, 0),
])
def test_solutions(args, expected):
    assert Solution().findNthDigit(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
