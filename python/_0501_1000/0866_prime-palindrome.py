#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:16:22
# @Last Modified : 2020-05-05 22:16:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 求出大于或等于 N 的最小回文素数。
#
#  回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。
#
#  例如，2，3，5，7，11 以及 13 是素数。
#
#  回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。
#
#  例如，12321 是回文数。
#
#
#
#  示例 1：
#
#  输入：6
# 输出：7
#
#
#  示例 2：
#
#  输入：8
# 输出：11
#
#
#  示例 3：
#
#  输入：13
# 输出：101
#
#
#
#  提示：
#
#
#  1 <= N <= 10^8
#  答案肯定存在，且小于 2 * 10^8。
#
#
#
#
#
#  Related Topics 数学
#  👍 47 👎 0

import pytest


class Solution:

    def primePalindrome(self, N: int) -> int:
        """ 不存在 8 长度的素数。"""
        def is_prime(n):
            return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans


        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8


@pytest.mark.parametrize("args,expected", [
    (6, 7),
    (8, 11),
    (13, 101),
])
def test_solutions(args, expected):
    assert Solution().primePalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
