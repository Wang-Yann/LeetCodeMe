#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 17:11:04
# @Last Modified : 2020-04-25 17:11:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    ]
    res = [sol.evalRPN(args) for args in samples]
    print(res)
