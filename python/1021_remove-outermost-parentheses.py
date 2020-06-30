#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"
# ，"(())()" 和 "(()(()))" 都是有效的括号字符串。 
# 
#  如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。 
# 
#  给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。 
# 
#  对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。 
# 
#  
# 
#  示例 1： 
# 
#  输入："(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。 
# 
#  示例 2： 
# 
#  输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
#  
# 
#  示例 3： 
# 
#  输入："()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 10000 
#  S[i] 为 "(" 或 ")" 
#  S 是一个有效括号字符串 
#  
#  Related Topics 栈

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        level = 0
        ans = []
        for char in S:
            if char == ")":
                level -= 1
            if level >= 1:
                ans.append(char)
            if char == "(":
                level += 1
        # print(ans)
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ''
        for char in S:
            if char == '(':
                stack.append(char)
                if len(stack) > 1:
                    result += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    result += ')'
        return result


@pytest.mark.parametrize("args,expected", [
    ("(()())(())", "()()()"),
    ("(()())(())(()(()))", "()()()()(())"),
    ("()()", ""),
])
def test_solutions(args, expected):
    assert Solution().removeOuterParentheses(args) == expected
    assert Solution1().removeOuterParentheses(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
