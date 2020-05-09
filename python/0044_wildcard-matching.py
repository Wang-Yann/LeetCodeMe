#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。 
# 
#  '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#  
# 
#  两个字符串完全匹配才算匹配成功。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。 
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
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#  
# 
#  示例 5: 
# 
#  输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false 
#  Related Topics 贪心算法 字符串 动态规划 回溯算法

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """DP
    TODO
    dp[p_idx][s_idx] 代表的是字符模式中的第 p_idx 字符和输入字符串的第 s_idx 字符是否匹配。
    """
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1,len(s) + 1):
            dp[i][0] = False
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[len(s)][len(p)]


# leetcode submit region end(Prohibit modification and deletion)

class Solution4(object):
    """官方　带记忆的递归"""

    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0], ]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    def helper(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = self.helper(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s, p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]

    def isMatch(self, s, p):
        p = self.remove_duplicate_stars(p)
        # memorization hashmap to be used during the recursion
        self.dp = {}
        return self.helper(s, p)


@pytest.mark.parametrize("s,p,expected", [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("", "*", True),
])
def test_solutions(s, p, expected):
    # assert Solution4().isMatch(s, p) == expected
    assert Solution().isMatch(s,p) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
