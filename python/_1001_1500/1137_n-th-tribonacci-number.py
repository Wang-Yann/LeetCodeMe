#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
#  Related Topics 递归

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):

    def tribonacci(self, n):
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def tribonacci(self, n: int) -> int:
        t3 = [0, 1, 1]
        if n <= 2:
            return t3[n]
        a, b, c = t3
        for _ in range(2, n):
            a, b, c = b, c, a + b + c
        return c


@pytest.mark.parametrize("args,expected", [
    (4, 4),
    pytest.param(25, 1389537),
])
def test_solutions(args, expected):
    assert Solution().tribonacci(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
