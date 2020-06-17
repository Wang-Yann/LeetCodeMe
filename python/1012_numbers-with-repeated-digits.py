#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数的个数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
#  
# 
#  示例 2： 
# 
#  输入：100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
#  
# 
#  示例 3： 
# 
#  输入：1000
# 输出：262
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10^9 
#  
#  Related Topics 数学 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numDupDigitsAtMostN(self, N: int) -> int:
        """
        数位DP
        至少有一位重复数字的反面就是：所有数字都不一样。

        """

        def A(m, n):
            res = 1
            while n > 0:
                res *= m - n + 1
                n -= 1
            return res

        digits = list(map(int, str(N + 1)))
        ans = 0
        # Given 321
        #
        # 1. count numbers without repeated digits:
        # - X
        # - XX
        for i in range(1, len(digits)):
            ans += A(9, 1) * A(9, i - 1)
        # 2. count numbers without repeated digits:
        # - 1XX ~ 3XX
        # - 30X ~ 32X
        # - 320 ~ 321
        prefix_set = set()
        for i, x in enumerate(digits):
            for y in range(1 if i == 0 else 0, x):
                if y in prefix_set:
                    continue
                ans += A(9 - i, len(digits) - i - 1)
            if x in prefix_set:
                break
            prefix_set.add(x)
        return N - ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (20, 1),
    (100, 10),
    (1000, 262),
])
def test_solutions(args, expected):
    assert Solution().numDupDigitsAtMostN(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
