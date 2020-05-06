#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        GOOD
        对于遇到的每个( ，我们将它的下标放入栈中。
        对于遇到的每个 ) ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，得出当前有效括号字符串的长度

        """
        ans = 0
        stack = [-1]
        for idx, char in enumerate(s):
            if s[idx] == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    ans = max(ans, idx - stack[-1])
        return ans


# leetcode submit region end(Prohibit mod
#
#
# ification and deletion)

class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        length = len(s)
        dp = [0] * length
        for i in range(1, length):
            if s[i] == ")":
                if s[i-1]=="(":
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i > dp[i - 1] and s[i - dp[i-1] - 1] == "(":
                    if (i - dp[i - 1]) >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
                ans = max(ans, dp[i])
        return ans


@pytest.mark.parametrize("args,expected", [
    ("(()", 2),
    (")()())", 4),
    ("())((())", 4),
])
def test_solutions(args, expected):
    assert Solution().longestValidParentheses(args) == expected
    assert Solution1().longestValidParentheses(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
