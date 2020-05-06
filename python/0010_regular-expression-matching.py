#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
#  Related Topics 字符串 动态规划 回溯算法

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        f_match = bool(s) and p[0] in [s[0], "."]
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (
                    f_match and self.isMatch(s[1:], p)
            )
        else:
            return f_match and self.isMatch(s[1:], p[1:])


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], "."}
                if j + 1 < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="aa", p="a"), False),
    (dict(s="aa", p="a*"), True),
    (dict(s="ab", p=".*"), True),
    (dict(s="aab", p="c*a*b"), True),
    (dict(s="mississippi", p="mis*is*p*."), False),
    (dict(s="ab", p=".*c"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isMatch(**kwargs) == expected
    assert Solution1().isMatch(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
