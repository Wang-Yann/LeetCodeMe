#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 *
#  3 * 2 * 1。 
# 
#  相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)
# 和减法(-)。 
# 
#  例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我
# 们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。 
# 
#  另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。 
# 
#  实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。 
# 
#  
# 
#  示例 1： 
# 
#  输入：4
# 输出：7
# 解释：7 = 4 * 3 / 2 + 1
#  
# 
#  示例 2： 
# 
#  输入：10
# 输出：12
# 解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10000 
#  -2^31 <= answer <= 2^31 - 1 （答案保证符合 32 位整数。） 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def clumsy(self, N: int) -> int:
        N4 = N // 4
        ans = 0
        if N >= 4:
            ans = N * (N - 1) // (N - 2) + (N - 3)
            for i in range(1, N4):
                ans = ans - (N - 4 * i) * (N - 4 * i - 1) // (N - 4 * i - 2)
                ans = ans + (N - 4 * i - 3)
            if N % 4 == 3:
                ans -= 6
            elif N % 4 == 2:
                ans -= 2
            elif N % 4 == 1:
                ans -= 1
        elif N == 3:
            return 6
        elif N == 2:
            return 2
        elif N == 1:
            return 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# observation:
# i*(i-1)/(i-2) = i+1+2/(i-2)
#     if i = 3  => i*(i-1)/(i-2) = i + 3
#     if i = 4  => i*(i-1)/(i-2) = i + 2
#     if i >= 5 => i*(i-1)/(i-2) = i + 1
# clumsy(N):
#     if N = 1 => N
#     if N = 2 => N
#     if N = 3 => N + 3
#     if N = 4 => N + 2 + 1 = N + 3
#     if N > 4 and N % 4 == 1 => N + 1 + (... = 0) + 2 - 1           = N + 2
#     if N > 4 and N % 4 == 2 => N + 1 + (... = 0) + 3 - 2 * 1       = N + 2
#     if N > 4 and N % 4 == 3 => N + 1 + (... = 0) + 4 - 3 * 2 / 1   = N - 1
#     if N > 4 and N % 4 == 0 => N + 1 + (... = 0) + 5 - (4*3/2) + 1 = N + 1

class Solution1(object):

    def clumsy(self, N):
        if N <= 2:
            return N
        if N <= 4:
            return N + 3

        if N % 4 == 0:
            return N + 1
        elif N % 4 <= 2:
            return N + 2
        return N - 1


@pytest.mark.parametrize("args,expected", [
    (4, 7),
    pytest.param(10, 12),
])
def test_solutions(args, expected):
    assert Solution().clumsy(args) == expected
    assert Solution1().clumsy(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
