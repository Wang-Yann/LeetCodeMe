#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 22:31:41
# @Last Modified : 2020-04-26 22:31:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def scoreOfParentheses(self, S: str) -> int:
        """
        我们用一个栈来维护当前所在的深度，以及每一层深度的得分。当我们遇到一个左括号 ( 时，
        我们将深度加一，并且新的深度的得分置为 0。当我们遇到一个右括号 ) 时，
        我们将当前深度的得分乘二并加到上一层的深度。这里有一种例外情况，如果遇到的是 ()，那么只将得分加一

    """
        stack = [0]
        for char in S:
            if char == "(":
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(1, 2 * last)
        # print(stack)
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "()", "(())", "()()", "(()(()))"

    ]
    res = [sol.scoreOfParentheses(args) for args in samples]
    print(res)
