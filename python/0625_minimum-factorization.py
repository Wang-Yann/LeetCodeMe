#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 16:59:45
# @Last Modified : 2020-07-30 16:59:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数 a，找出最小的正整数 b 使得 b 的所有数位相乘恰好等于 a。 
# 
#  如果不存在这样的结果或者结果不是 32 位有符号整数，返回 0。 
# 
#  
# 
#  样例 1 
# 
#  输入： 
# 
#  48 
#  
# 
#  输出： 
# 
#  68 
# 
#  
# 
#  样例 2 
# 
#  输入： 
# 
#  15
#  
# 
#  输出： 
# 
#  35 
# 
#  
#  Related Topics 递归 数学 
#  👍 15 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestFactorization(self, a: int) -> int:
        """AC"""
        if a < 10:
            return a
        factors = []
        for i in range(9, 1, -1):
            while a % i == 0:
                factors.append(i)
                a //= i
        if a != 1:
            return 0
        factors.sort()
        ans = int("".join(map(str, factors)))
        return ans if ans <= 0x7fffffff else 0


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def smallestFactorization(self, a):

        if a < 2:
            return a
        result, mul = 0, 1
        for i in reversed(range(2, 10)):
            while a % i == 0:
                a /= i
                result = mul * i + result
                mul *= 10
        return result if a == 1 and result < 2 ** 31 else 0


@pytest.mark.parametrize("args,expected", [
    (48, 68),
    (15, 35),
    (1, 1),
    (22, 0),
    (11, 0),
])
def test_solutions(args, expected):
    assert Solution().smallestFactorization(args) == expected
    assert Solution1().smallestFactorization(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
