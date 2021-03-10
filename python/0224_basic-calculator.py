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


class Solution(object):
    def calculate(self, s):
        if s.strip().startswith("-"):
            s = "0" + s
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)


class Solution1:

    def calculate(self, s: str) -> int:
        """
        如果我们使用栈并从左到右读取表达式的元素，则最终我们会从右到左计算表达式。就会出现 (A-B)-C 等于
        (C-B)-A的情况，这是不正确的。减法即不遵循结合律也不遵循交换律。
        """

        def compute():
            """重点 顺序是反的"""
            left = val_stack.pop()
            right = val_stack.pop()
            op = op_stack.pop()
            operator_map = {"+": operator.add, "-": operator.sub}
            if op in operator_map:
                val_stack.append(operator_map[op](left, right))

        if s.strip().startswith("-"):
            s = "0" + s
        val_stack = []
        op_stack = []
        N = len(s)
        i = N - 1
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
        return val_stack[0]


class Solution2(object):
    def calculate(self, s):
        """TLE"""

        def helper(chars):
            stack = []
            sign = '+'
            num = 0

            while len(chars) > 0:
                c = chars.pop(0)
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归计算 num
                if c == '(':
                    num = helper(chars)

                if c in ("+", "-", "*", "/", ")") or not chars:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # python 除法向 0 取整的写法
                        stack[-1] = int(stack[-1] // float(num))
                    num = 0
                    sign = c
                # 遇到右括号返回递归结果
                if c == ')':
                    break

            return sum(stack)

        # 需要把字符串转成列表方便操作
        return helper(list(s))


@pytest.mark.parametrize("args,expected", [
    ["1 + 11", 12],
    [" 2-1 + 2 ", 3],
    ["(1+(4+5+2)-3)+(6+8)", 23],
    ["(1)", 1],
    ["1+5-4", 2],
    ["2-4-(8+2-6+(8+4-1+8-10))", -15],
    ["2-4-(8+2-6+(8+4-(1)+8-10))", -15],
    ["-2+1", -1],
    [" -2+1", -1],
])
@pytest.mark.parametrize("SolutionCLS", [Solution1, Solution, Solution2])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().calculate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
