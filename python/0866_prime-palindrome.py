#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:16:22
# @Last Modified : 2020-05-05 22:16:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
