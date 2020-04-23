#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:58:10
# @Last Modified : 2020-04-23 23:58:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n
        fb = [0] * (n + 1)
        fb[1] = 1
        for i in range(2, n + 1):
            fb[i] = fb[i - 2] + fb[i - 1]
        return fb[n] % 1000000007

    def fib1(self, n: int) -> int:
        if n in (0, 1):
            return n
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = a + b, a
        mod = 1000000007
        return a % mod


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 5, 45
    ]
    res = [sol.fib(args) for args in samples]
    print(res)
