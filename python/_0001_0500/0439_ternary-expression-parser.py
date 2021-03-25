#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 18:50:24
# @Last Modified : 2020-07-28 18:50:24
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个以字符串表示的任意嵌套的三元表达式，计算表达式的值。你可以假定给定的表达式始终都是有效的并且只包含数字 0-9, ?, :, T 和 F (T 和 
# F 分别表示真和假）。 
# 
#  注意： 
# 
#  
#  给定的字符串长度 ≤ 10000。 
#  所包含的数字都只有一位数。 
#  条件表达式从右至左结合（和大多数程序设计语言类似）。 
#  条件是 T 和 F其一，即条件永远不会是数字。 
#  表达式的结果是数字 0-9, T 或者 F。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入： "T?2:3"
# 
# 输出： "2"
# 
# 解释： 如果条件为真，结果为 2；否则，结果为 3。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入： "F?1:T?4:5"
# 
# 输出： "4"
# 
# 解释： 条件表达式自右向左结合。使用括号的话，相当于：
# 
#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
# 
#           -> "(F ? 1 : 4)"                 或者     -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"
#  
# 
#  
# 
#  示例 3： 
# 
#  输入： "T?T?F:5:3"
# 
# 输出： "F"
# 
# 解释： 条件表达式自右向左结合。使用括号的话，相当于：
# 
#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
# 
#           -> "(T ? F : 3)"                 或者       -> "(T ? F : 5)"
#           -> "F"                                     -> "F"
#  
# 
#  
#  Related Topics 栈 深度优先搜索 
#  👍 23 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def parseTernary(self, expression: str) -> str:
        N = len(expression)
        level = 0
        for j in range(1, N):
            if expression[j] == "?":
                level += 1
            elif expression[j] == ":":
                level -= 1
            if level == 0:
                if expression[0] == 'T':
                    return self.parseTernary(expression[2:j])
                else:
                    return self.parseTernary(expression[j + 1: N])
        return expression


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def parseTernary(self, expression: str) -> str:
        """用栈从后往前，遇到数字放进栈里。 遇到T就保留栈顶的，删掉第二个。 遇到F就删除栈顶的，保留第二个"""
        stack = []
        i = len(expression) - 1
        while i >= 1:
            if expression[i] == "?":
                left = stack.pop()
                right = stack.pop()
                stack.append(left if expression[i - 1] == "T" else right)
                i -= 1
            elif expression[i] != ":":
                stack.append(expression[i])
            i -= 1
        return stack[0]


@pytest.mark.parametrize("args,expected", [
    ("T?2:3", "2"),
    ("F?1:T?4:5", "4"),
    ("T?T?F:5:3", "F"),
])
def test_solutions(args, expected):
    assert Solution().parseTernary(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
