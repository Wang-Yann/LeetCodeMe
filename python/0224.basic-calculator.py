#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:59:20
# @Last Modified : 2020-04-25 19:59:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import operator


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
            operator_map = {"+":operator.add, "-":operator.sub}
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




if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1 + 11",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
        "(1)",
        "1+5-4",
        "2-4-(8+2-6+(8+4-1+8-10))",
        "2-4-(8+2-6+(8+4-(1)+8-10))"

    ]
    res = [sol.calculate(args) for args in samples]
    print(res)
