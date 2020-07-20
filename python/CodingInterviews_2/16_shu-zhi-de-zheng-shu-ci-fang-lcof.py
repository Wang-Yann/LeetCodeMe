#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 21:44:10
# @Last Modified : 2020-05-02 21:44:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数
# 问题。
#
#
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
#
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/
#  Related Topics 递归
#  👍 47 👎 0


import pytest


class Solution:

    def myPow(self, x: float, n: int) -> float:
        def helper(x,abs_n):
            if abs_n == 0:
                return 1
            if abs_n == 1:
                return x
            ans = helper(x, abs_n >> 1)
            ans *= ans
            if abs_n & 0b1 == 1:
                ans *= x
            return ans
        res = helper(x,abs(n))
        if n<0:
            res=1.0/res
        return res


@pytest.mark.parametrize("x,n,expected", [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25),
    (8.95371, -1,0.1116855),
])
def test_solutions(x, n, expected):
    assert Solution().myPow(x, n) == pytest.approx(expected, 0.001)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
