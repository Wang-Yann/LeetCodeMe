#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 00:01:49
# @Last Modified : 2020-07-27 00:01:49
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 实现一个基本的计算器来计算简单的表达式字符串。 
# 
#  表达式字符串可以包含左括号 ( 和右括号 )，加号 + 和减号 -，非负 整数和空格 。 
# 
#  表达式字符串只包含非负整数， +, -, *, / 操作符，左括号 ( ，右括号 )和空格 。整数除法需要向下截断。 
# 
#  你可以假定给定的字符串总是有效的。所有的中间结果的范围为 [-2147483648, 2147483647]。 
# 
#  
# 
#  一些例子： 
# 
#  "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#  
# 
#  
# 
#  注：不要 使用内置库函数 eval。 
# 
#  
#  Related Topics 栈 字符串 
#  👍 28 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def calculate(self, s: str) -> int:
        operands, operators = [], []
        operand = ""
        for i in range(len(s) - 1, -1, -1):
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

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left // right)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def __init__(self):
        self.i = 0

    def parseExpr(self, s):
        nums = []
        op = '+'
        while self.i < len(s) and op != ')':  # 遇到右括号退出递归
            if s[self.i] == ' ':
                self.i += 1
                continue
            if s[self.i] == '(':  # 遇到左括号进入递归
                self.i += 1
                n = self.parseExpr(s)
            else:
                n = self.parseNum(s)  # 字符串转化数字
            if op == '+':  # 加法
                nums.append(n)
            elif op == '-':  # 减法
                nums.append(-n)
            elif op == '*':  # 乘法
                nums[-1] *= n
            elif op == '/':  # 除法
                nums[-1] //= n
            if self.i >= len(s):
                break
            op = s[self.i]
            self.i += 1
        res = 0
        for n in nums:
            res += n
        return res

    def parseNum(self, s):
        n = 0
        while self.i < len(s) and '0' <= s[self.i] <= '9':
            n = ord(s[self.i]) - ord('0') + 10 * n
            self.i += 1
        return n

    def calculate(self, s):
        # Write your code here
        return self.parseExpr(s)


class Solution00(object):
    def calculate(self, s):
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
    ("1 + 1", 2),
    (" 6-4 / 2 ", 4),
    ("2*(5+5*2)/3+(6/2+8)", 21),
    ("(2+6* 3+5- (3*14/7+2)*5)+3", -12),
])
@pytest.mark.parametrize("SolutionCLS", [Solution1, Solution, Solution00])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().calculate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
