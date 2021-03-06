#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 17:11:04
# @Last Modified : 2020-04-25 17:11:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 根据 逆波兰表示法，求表达式的值。
#
#  有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
#
#
#  说明：
#
#
#  整数除法只保留整数部分。
#  给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
#
#
#
#
#  示例 1：
#
#  输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
#
#
#  示例 2：
#
#  输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
#
#
#  示例 3：
#
#  输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释:
# 该算式转化为常见的中缀算术表达式为：
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
#  逆波兰表达式：
#
#  逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
#
#
#  平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
#  该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
#
#
#  逆波兰表达式主要有以下两个优点：
#
#
#  去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
#  适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
#
#  Related Topics 栈
#  👍 167 👎 0
import operator
from typing import List

import pytest


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        """
        python除法负数商的取整方式与C++不同
        """
        # numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        if not tokens:
            return
        stack = []
        for token in tokens:
            if token == "+":
                val = stack.pop()
                stack.append(stack.pop() + val)
            elif token == "-":
                val = stack.pop()
                stack.append(stack.pop() - val)
            elif token == "*":
                val = stack.pop()
                stack.append(stack.pop() * val)
            elif token == "/":
                val = stack.pop()
                divider = stack.pop()
                flag = -1 if val * divider < 0 else 1
                res = abs(divider) // abs(val)
                stack.append(res * flag)
            else:
                stack.append(int(token))
        # print(stack)
        return int(stack.pop())


class Solution1:

    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),  # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]


@pytest.mark.parametrize("args,expected", [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().evalRPN(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
