#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。 
# 
#  （注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。） 
# 
#  示例 1: 
# 
#  
# 输入: L = 6, R = 10
# 输出: 4
# 解释:
# 6 -> 110 (2 个计算置位，2 是质数)
# 7 -> 111 (3 个计算置位，3 是质数)
# 9 -> 1001 (2 个计算置位，2 是质数)
# 10-> 1010 (2 个计算置位，2 是质数)
#  
# 
#  示例 2: 
# 
#  
# 输入: L = 10, R = 15
# 输出: 5
# 解释:
# 10 -> 1010 (2 个计算置位, 2 是质数)
# 11 -> 1011 (3 个计算置位, 3 是质数)
# 12 -> 1100 (2 个计算置位, 2 是质数)
# 13 -> 1101 (3 个计算置位, 3 是质数)
# 14 -> 1110 (3 个计算置位, 3 是质数)
# 15 -> 1111 (4 个计算置位, 4 不是质数)
#  
# 
#  注意: 
# 
#  
#  L, R 是 L <= R 且在 [1, 10^6] 中的整数。 
#  R - L 的最大值为 10000。 
#  
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        """
          len(bin(10**6))＝22
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}

        def bitCount(n):
            res = 0
            while n:
                n &= (n - 1)
                res += 1
            return res

        return sum(bitCount(x) in primes for x in range(L, R + 1))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    # [dict(L=6, R=10), 4],
    [dict(L=10, R=15), 5],
])
def test_solutions(kw, expected):
    assert Solution().countPrimeSetBits(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
