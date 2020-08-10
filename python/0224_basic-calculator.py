#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:59:20
# @Last Modified : 2020-04-25 19:59:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
#  字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格 。
#
#  示例 1:
#
#  输入: "1 + 1"
# 输出: 2
#
#
#  示例 2:
#
#  输入: " 2-1 + 2 "
# 输出: 3
#
#  示例 3:
#
#  输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
#
#  说明：
#
#
#  你可以假设所给定的表达式都是有效的。
#  请不要使用内置的库函数 eval。
#
#  Related Topics 栈 数学
#  👍 225 👎 0

"""

import operator

import pytest


class Solution:

    def calculate(self, s: str) -> int:
        """
        如果我们使用栈并从左到右读取表达式的元素，则最终我们会从右到左计算表达式。就会出现 (A-B)-C(A−B)−C 等于
        (C-B)-A(C−B)−A 的情况，这是不正确的。减法即不遵循结合律也不遵循交换律。
        """

        def compute():
            """重点 顺序是反的"""
            left = val_stack.pop()
            right = val_stack.pop()
            op = op_stack.pop()
            operator_map = {"+": operator.add, "-": operator.sub}
            if op in operator_map:
                val_stack.append(operator_map[op](left, right))

        val_stack = []
        op_stack = []
        length = len(s)
        i = length - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            elif s[i] in ("+", "-", ")"):
                op_stack.append(s[i])
                i -= 1
            elif s[i] == "(":
                while op_stack[-1] != ")":
                    compute()
                op_stack.pop()
                i -= 1
            else:
                j = i
                while j >= 0 and s[j].isdigit():
                    j -= 1
                token = s[j + 1:i + 1]
                val_stack.append(int(token))
                i = j

        while op_stack:
            compute()
        # print("after", val_stack, op_stack)
        return val_stack[0]


@pytest.mark.parametrize("args,expected", [
    ["1 + 11", 12],
    [" 2-1 + 2 ", 3],
    ["(1+(4+5+2)-3)+(6+8)", 23],
    ["(1)", 1],
    ["1+5-4", 2],
    ["2-4-(8+2-6+(8+4-1+8-10))", -15],
    ["2-4-(8+2-6+(8+4-(1)+8-10))", -15],
])
def test_solutions(args, expected):
    assert Solution().calculate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
