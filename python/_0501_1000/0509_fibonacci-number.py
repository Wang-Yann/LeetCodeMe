#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： 
# 
#  F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
#  
# 
#  给定 N，计算 F(N)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
#  
# 
#  示例 2： 
# 
#  输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
#  
# 
#  示例 3： 
# 
#  输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 ≤ N ≤ 30 
#  
#  Related Topics 数组

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N in (1, 2):
            return 1
        a, b = 1, 1
        for i in range(3, N + 1):
            a, b = a + b, a
        return a


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (0, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_solutions(args, expected):
    assert Solution().fib(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
