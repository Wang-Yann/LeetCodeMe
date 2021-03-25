#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数 x，我们将会写出一个形如 x (op1) x (op2) x (op3) x ... 的表达式，其中每个运算符 op1，op2，… 可以是加
# 、减、乘、除（+，-，*，或是 /）之一。例如，对于 x = 3，我们可以写出表达式 3 * 3 / 3 + 3 - 3，该式的值为 3 。 
# 
#  在写这样的表达式时，我们需要遵守下面的惯例： 
# 
#  
#  除运算符（/）返回有理数。 
#  任何地方都没有括号。 
#  我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。 
#  不允许使用一元否定运算符（-）。例如，“x - x” 是一个有效的表达式，因为它只使用减法，但是 “-x + x” 不是，因为它使用了否定运算符。 
#  
# 
#  我们希望编写一个能使表达式等于给定的目标值 target 且运算符最少的表达式。返回所用运算符的最少数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：x = 3, target = 19
# 输出：5
# 解释：3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。
#  
# 
#  示例 2： 
# 
#  输入：x = 5, target = 501
# 输出：8
# 解释：5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。
#  
# 
#  示例 3： 
# 
#  输入：x = 100, target = 100000000
# 输出：3
# 解释：100 * 100 * 100 * 100 。表达式包含 3 个运算符。 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= x <= 100 
#  1 <= target <= 2 * 10^8 
#  
# 
#  
#  Related Topics 数学 动态规划

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
         我们可以使用动态规划自顶向下地计算 dp(i, target)。这里的 i 表示我们正在考虑使用 x^i
         https://leetcode-cn.com/problems/least-operators-to-express-number/solution/biao-shi-shu-zi-de-zui-shao-yun-suan-fu-by-leetcod/
        """
        cost = list(range(40))
        cost[0] = 2

        @functools.lru_cache(None)
        def dp(i, targ):
            if targ == 0:
                return 0
            if targ == 1:
                return cost[i]
            if i >= 40 - 1:
                return float("inf")
            t, r = divmod(targ, x)
            return min(r * cost[i] + dp(i + 1, t), (x - r) * cost[i] + dp(i + 1, t + 1))
        # print(cost)
        return dp(0, target) - 1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    # [dict(x=3, target=19), 5],
    [dict(x=5, target=501), 8],
    # [dict(x=100, target=100000000), 3],
])
def test_solutions(kw, expected):
    assert Solution().leastOpsExpressTarget(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
