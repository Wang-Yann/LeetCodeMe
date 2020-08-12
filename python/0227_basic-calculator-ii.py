#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:59:20
# @Last Modified : 2020-04-25 19:59:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
#  字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。
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
#  👍 157 👎 0

import operator

import pytest


class Solution1:

    def calculate(self, s: str) -> int:
        """
        重点 顺序
        """
        operator_map = {"+": operator.add, "*": operator.mul,
                        "-": operator.sub, "/": operator.floordiv}
        val_stack = []
        op_stack = []
        length = len(s)
        i = 0
        while i <= length - 1:
            if s[i] == " ":
                i += 1
                continue
            elif s[i] in ("*", "/"):
                op_stack.append(s[i])
                i += 1
            elif s[i] in ("+", "-", "*", "/"):
                op_stack.append(s[i])
                i += 1
            else:
                j = i
                while j <= length - 1 and s[j].isdigit():
                    j += 1
                token = s[i:j]
                val_stack.append(int(token))
                while op_stack and op_stack[-1] in '*/':
                    right = val_stack.pop()
                    left = val_stack.pop()
                    op = op_stack.pop()
                    if op in operator_map:
                        val_stack.append(operator_map[op](left, right))
                i = j
        val_stack.reverse()
        op_stack.reverse()
        while op_stack:
            left = val_stack.pop()
            right = val_stack.pop()
            op = op_stack.pop()
            if op in operator_map:
                val_stack.append(operator_map[op](left, right))
        return val_stack[0]


class Solution(object):

    def calculate(self, s: str) -> int:
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[0]

    def compute(self, operands, operators):
        left = operands.pop()
        right = operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left // right)


@pytest.mark.parametrize(
    "args,expected",
    list(zip(
        [
            "1 -1+1",
            " 2-1 + 2 ",
            "3+2*2-6",
            "1+5-4",
            " 3/2 ",
            " 3+5 / 2 ",
            "14/3*2",
            "1+1+1"

        ], [1, 3, 1, 2, 1, 5, 8, 3]
    ))
)
def test_solutions(args, expected):
    assert Solution().calculate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
