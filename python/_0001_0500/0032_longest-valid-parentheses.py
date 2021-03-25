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
        终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」

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


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        length = len(s)
        dp = [0] * length
        for i in range(1, length):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i > dp[i - 1] and s[i - dp[i - 1] - 1] == "(":
                    if (i - dp[i - 1]) >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
                ans = max(ans, dp[i])
        return ans


class Solution2:

    def longestValidParentheses(self, s: str) -> int:
        """
        GOOD
        例如：s = )(()())，我们用栈可以找到，
        位置 2 和位置 3 匹配，
        位置 4 和位置 5 匹配，
        位置 1 和位置 6 匹配，
        这个数组为：2,3,4,5,1,6 这是通过栈找到的，我们按递增排序！1,2,3,4,5,6
        找出该数组的最长连续数列的长度就是最长有效括号长度！

        """
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        # print(res)
        res.sort()
        i = 0
        ans = 0
        N = len(res)
        while i < N:
            j = i
            while j < N - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans


@pytest.mark.parametrize("args,expected", [
    ("(()", 2),
    (")()())", 4),
    ("())((())", 4),
])
def test_solutions(args, expected):
    assert Solution().longestValidParentheses(args) == expected
    assert Solution1().longestValidParentheses(args) == expected
    assert Solution2().longestValidParentheses(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
