#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:26:39
# @Last Modified : 2020-05-04 20:26:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def countPrimes(self, n: int) -> int:
        """ 厄拉多塞筛法"""
        if n <= 2:
            return 0
        is_prime = [True] * (n // 2)
        cnt = len(is_prime)
        for i in range(3, n, 2):
            if i * i >= n:
                break
            if not is_prime[i // 2]:
                continue
            for j in range(i ** 2, n, 2 * i):
                if not is_prime[j // 2]:
                    continue
                cnt -= 1
                is_prime[j // 2] = False
        return cnt


class Solution1:

    def countPrimes(self, n: int) -> int:
        """ 厄拉多塞筛法"""
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i:n:i] = [False] * len(primes[i * i:n:i])
        return sum(primes)


@pytest.mark.parametrize("args,expected", [
    (10, 4),
    pytest.param(12, 5),
])
def test_solutions(args, expected):
    assert Solution().countPrimes(args) == expected
    assert Solution1().countPrimes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
