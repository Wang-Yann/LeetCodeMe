#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 18:42:21
# @Last Modified : 2020-05-03 18:42:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
"""
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划
#  👍 2437 👎 0

"""

import pytest


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """中心扩展"""

        def expandAroundCenter(left, right):
            while left >= 0 and right <= length - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        length = len(s)
        if not s:
            return ""
        start, end = 0, 0
        for i in range(length):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]


class Solution1:

    def longestPalindrome(self, s: str) -> str:
        """
        动态规划
        初始状态，l=r 时，此时 dp[l][r]=true。
        状态转移方程，dp[l][r]=true 并且(l-1)和（r+1)两个位置为相同的字符，此时 dp[l-1][r+1]=true
        https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode/
        """
        length = len(s)
        if len(s) < 2:
            return s
        # 最长回文串的起点,终点，长度
        max_start = 0
        max_end = 0
        max_len = 1
        dp = [[False] * length for _ in range(length)]
        for r in range(1, length):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if r - l + 1 > max_len:
                        max_len = r - l + 1
                        max_start = l
                        max_end = r
        return s[max_start:max_end + 1]


class Solution2:

    def longestPalindrome(self, s: str) -> str:
        """
        Manacher
        """

        def pre_process(s):
            res = "#".join(s)
            return "^#" + res + "#$"

        t = pre_process(s)
        P = [0] * len(t)
        center, right = 0, 0
        for i in range(1, len(t) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > right:
                center, right = i, i + P[i]
        max_i = 0
        # print(P)
        for i in range(1, len(t) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) // 2
        return s[start:start + P[max_i]]


@pytest.mark.parametrize("args,expected", [
    ("babad", ["bab", "aba"]),
    pytest.param("cbbd", ["bb"]),
])
def test_solutions(args, expected):
    assert Solution().longestPalindrome(args) in expected
    assert Solution1().longestPalindrome(args) in expected
    assert Solution2().longestPalindrome(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
