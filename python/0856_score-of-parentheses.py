#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 22:31:41
# @Last Modified : 2020-04-26 22:31:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
#
#  () 得 1 分。
#  AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
#  (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#
#
#
#
#  示例 1：
#
#  输入： "()"
# 输出： 1
#
#
#  示例 2：
#
#  输入： "(())"
# 输出： 2
#
#
#  示例 3：
#
#  输入： "()()"
# 输出： 2
#
#
#  示例 4：
#
#  输入： "(()(()))"
# 输出： 6
#
#
#
#
#  提示：
#
#
#  S 是平衡括号字符串，且只含有 ( 和 ) 。
#  2 <= S.length <= 50
#
#  Related Topics 栈 字符串
#  👍 122 👎 0

"""


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
