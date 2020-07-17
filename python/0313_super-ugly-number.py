#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 22:37:05
# @Last Modified : 2020-05-04 22:37:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 编写一段程序来查找第 n 个超级丑数。
#
#  超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
#
#  示例:
#
#  输入: n = 12, primes = [2,7,13,19]
# 输出: 32
# 解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26
# ,28,32] 。
#
#  说明:
#
#
#  1 是任何给定 primes 的超级丑数。
#  给定 primes 中的数字以升序排列。
#  0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
#  第 n 个超级丑数确保在 32 位有符整数范围内。
#
#  Related Topics 堆 数学
#  👍 92 👎 0

import heapq
from typing import List

import pytest


class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        n -= 1
        while n:
            tmp = heapq.heappop(heap)
            while heap and tmp == heap[0]:
                tmp = heapq.heappop(heap)
            for p in primes:
                t = p * tmp
                heapq.heappush(heap, t)
            n -= 1
        return heapq.heappop(heap)


class Solution1:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [0] * n
        uglies[0] = 1
        visited = set()
        visited.add(1)
        primes_to_uglies_loc = [0] * len(primes)
        heap = []
        for idx, prime in enumerate(primes):
            heapq.heappush(heap, [prime, idx])
            visited.add(prime)

        for i in range(1, n):
            uglies[i], k = heapq.heappop(heap)

            while primes[k] * uglies[primes_to_uglies_loc[k]] in visited:
                primes_to_uglies_loc[k] += 1
            heapq.heappush(heap, [primes[k] * uglies[primes_to_uglies_loc[k]], k])
            visited.add(primes[k] * uglies[primes_to_uglies_loc[k]])
        return uglies[-1]


# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(k^2)
# TLE due to the last test case, but it passess and performs well in C++.
class Solution5(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        TODO
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for p in primes:
            heapq.heappush(heap, p)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            for i in range(len(primes)):
                if ugly_number % primes[i] == 0:
                    for j in range(i + 1):
                        heapq.heappush(heap, ugly_number * primes[j])
                    break

        return ugly_number


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=12, primes=[2, 7, 13, 19]), 32)
])
def test_solutions(kwargs, expected):
    assert Solution().nthSuperUglyNumber(**kwargs) == expected
    assert Solution1().nthSuperUglyNumber(**kwargs) == expected
    assert Solution5().nthSuperUglyNumber(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
