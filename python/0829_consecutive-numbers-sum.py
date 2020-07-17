#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 20:51:37
# @Last Modified : 2020-05-05 20:51:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
#
#  示例 1:
#
#
# 输入: 5
# 输出: 2
# 解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
#
#  示例 2:
#
#
# 输入: 9
# 输出: 3
# 解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
#
#  示例 3:
#
#
# 输入: 15
# 输出: 4
# 解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
#  说明: 1 <= N <= 10 ^ 9
#  Related Topics 数学
#  👍 72 👎 0

"""

import math

import pytest


class Solution:

    def consecutiveNumbersSum(self, N: int) -> int:
        """
        2N=k(2x+k+1)
        简单数学


        # x + x+1 + x+2 + ... + x+l-1 = N = 2^k * M, where M is odd
        # => l*x + (l-1)*l/2 = 2^k * M
        # => x = (2^k * M -(l-1)*l/2)/l= 2^k * M/l - (l-1)/2 is integer
        # => l could be 2 or any odd factor of M (excluding M)
        #    s.t. x = 2^k * M/l - (l-1)/2 is integer, and also unique
        # => the answer is the number of all odd factors of M
        # if prime factorization of N is 2^k * p1^a * p2^b * ..
        # => answer is the number of all odd factors = (a+1) * (b+1) * ...
        """
        ans = 1
        for i in range(2, int(math.sqrt(2 * N))+1):
            if (N - i * (i - 1) / 2) % i == 0:
                ans += 1
        return ans


@pytest.mark.parametrize("args,expected", [
    (5, 2),
    (9, 3),
    (15, 4),
])
def test_solutions(args, expected):
    assert Solution().consecutiveNumbersSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
