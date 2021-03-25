#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 S 和 T，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 true；否则，返回 false。字符串中可以使用括号来表示有理
# 数的重复部分。 
# 
#  通常，有理数最多可以用三个部分来表示：整数部分 <IntegerPart>、小数非重复部分 <NonRepeatingPart> 和小数重复部分 <(><
# RepeatingPart><)>。数字可以用以下三种方法之一来表示： 
# 
#  
#  <IntegerPart>（例：0，12，123） 
#  <IntegerPart><.><NonRepeatingPart> （例：0.5，2.12，2.0001） 
#  <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>（例：0.1(6)，0.9(9)，0.00(
# 1212)） 
#  
# 
#  十进制展开的重复部分通常在一对圆括号内表示。例如： 
# 
#  1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66) 
# 
#  0.1(6) 或 0.1666(6) 或 0.166(66) 都是 1 / 6 的正确表示形式。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "0.(52)", T = "0.5(25)"
# 输出：true
# 解释：因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的
# 数字。
#  
# 
#  示例 2： 
# 
#  输入：S = "0.1666(6)", T = "0.166(66)"
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：S = "0.9(9)", T = "1."
# 输出：true
# 解释：
# "0.9(9)" 代表 0.999999999... 永远重复，等于 1 。[有关说明，请参阅此链接]
# "1." 表示数字 1，其格式正确：(IntegerPart) = "1" 且 (NonRepeatingPart) = "" 。 
# 
#  
# 
#  提示： 
# 
#  
#  每个部分仅由数字组成。 
#  整数部分 <IntegerPart> 不会以 2 个或更多的零开头。（对每个部分的数字没有其他限制）。 
#  1 <= <IntegerPart>.length <= 4 
#  0 <= <NonRepeatingPart>.length <= 4 
#  1 <= <RepeatingPart>.length <= 4 
#  
#  Related Topics 数学

"""

from fractions import Fraction

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        """
        https://leetcode-cn.com/problems/equal-rational-numbers/solution/xiang-deng-de-you-li-shu-by-leetcode/
        分数　等比数列求和
        例如　
        S = "0.(12)" 则　r=1/100
        S=12*r/(1-r)
        """

        def convertToFraction(s):
            if "." not in s:
                return Fraction(int(s), 1)
            i = s.find(".")
            ans = Fraction(int(s[:i]), 1)
            s = s[i + 1:]
            if "(" not in s:
                if s:
                    ans += Fraction(int(s), 10 ** len(s))
                return ans
            i = s.find("(")
            if i:
                ans += Fraction(int(s[:i]), 10 ** i)
            s = s[i + 1:-1]
            j = len(s)
            ans += Fraction(int(s), 10 ** i * (10 ** j - 1))
            return ans

        # print(convertToFraction(S), convertToFraction(T))
        return convertToFraction(S) == convertToFraction(T)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isRationalEqual(self, S: str, T: str) -> bool:
        """
       　　特色^^解法
        """

        def toNumber(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])

        return toNumber(S) == toNumber(T)


@pytest.mark.parametrize("kw,expected", [
    [dict(S="0.(52)", T="0.5(25)"), True],
    # [dict(S="0.1666(6)", T="0.166(66)"), True],
    # [dict(S="0.9(9)", T="1."), True],
])
def test_solutions(kw, expected):
    assert Solution().isRationalEqual(**kw) == expected
    assert Solution1().isRationalEqual(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
