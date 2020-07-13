#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:58:50
# @Last Modified : 2020-07-13 18:58:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。 
# 
#  表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。 
# 
#  示例 1: 
# 
#  输入: "3+2*2"
# 输出: 7
#  
# 
#  示例 2: 
# 
#  输入: " 3/2 "
# 输出: 1 
# 
#  示例 3: 
# 
#  输入: " 3+5 / 2 "
# 输出: 5
#  
# 
#  说明： 
# 
#  
#  你可以假设所给定的表达式都是有效的。 
#  请不要使用内置的库函数 eval。 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="3+2*2"), 7],
    [dict(s=" 3/2 "), 1],
    [dict(s=" 3+5 / 2 "), 5],
])
def test_solutions(kw, expected):
    assert Solution().calculate(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
