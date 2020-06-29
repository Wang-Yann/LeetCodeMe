#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在显示着数字的坏计算器上，我们可以执行以下两种操作： 
# 
#  
#  双倍（Double）：将显示屏上的数字乘 2； 
#  递减（Decrement）：将显示屏上的数字减 1 。 
#  
# 
#  最初，计算器显示数字 X。 
# 
#  返回显示数字 Y 所需的最小操作数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：X = 2, Y = 3
# 输出：2
# 解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
#  
# 
#  示例 2： 
# 
#  输入：X = 5, Y = 8
# 输出：2
# 解释：先递减，再双倍 {5 -> 4 -> 8}.
#  
# 
#  示例 3： 
# 
#  输入：X = 3, Y = 10
# 输出：3
# 解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.
#  
# 
#  示例 4： 
# 
#  输入：X = 1024, Y = 1
# 输出：1023
# 解释：执行递减运算 1023 次
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= X <= 10^9 
#  1 <= Y <= 10^9 
#  
#  Related Topics 贪心算法 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """
        Greedy
        逆向思维
        除了对 X 执行乘 2 或 减 1 操作之外，我们也可以对 Y 执行除 2（当 Y 是偶数时）或者加 1 操作
        当 Y 大于 X 时，如果它是奇数，我们执行加法操作，否则执行除法操作。之后，我们需要执行 X - Y 次加法操作以得到 X。
        """
        ans = 0
        while Y > X:
            ans += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
        return ans + X - Y


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(X=2, Y=3), 2],
    [dict(X=5, Y=8), 2],
    [dict(X=3, Y=10), 3],
    [dict(X=1024, Y=1), 1023],
])
def test_solutions(kw, expected):
    assert Solution().brokenCalc(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
