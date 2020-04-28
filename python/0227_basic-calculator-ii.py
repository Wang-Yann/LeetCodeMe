#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:59:20
# @Last Modified : 2020-04-25 19:59:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import operator


class Solution1:

    def calculate(self, s: str) -> int:
        """重点 顺序
        """
        operator_map = {"+":operator.add, "*":operator.mul,
                        "-":operator.sub, "/":operator.floordiv}
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
                while operators and \
                        (operators[-1] == '*' or operators[-1] == '/'):
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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1 -1+1",
        " 2-1 + 2 ",
        "3+2*2-6",
        "1+5-4",
        " 3/2 ",
        " 3+5 / 2 ",
        "14/3*2",
        "1+1+1"

    ]
    res = [sol.calculate(args) for args in samples]
    print(res)
