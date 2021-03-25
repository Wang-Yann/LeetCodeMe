#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 23:14:19
# @Last Modified : 2020-04-10 23:14:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
#  示例 1:
#
#  输入: 121
# 输出: true
#
#
#  示例 2:
#
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
#  示例 3:
#
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
#  进阶:
#
#  你能不将整数转为字符串来解决这个问题吗？
#  Related Topics 数学

"""

import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def isPalindromeS(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse


@pytest.mark.parametrize("args,expected", [
    (121, True),
    (1, True),
    (11, True),
    (0, True),
    (1221, True),
    (434, True),
    (-1, False),
    (10, False),
    (1234, False),
])
def test_solutions(args, expected):
    assert Solution().isPalindrome(args) == expected
    assert Solution().isPalindromeS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
