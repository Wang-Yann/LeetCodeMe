#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 20:48:11
# @Last Modified : 2020-04-08 20:48:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 实现 strStr() 函数。
#
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。
#
#  示例 1:
#
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
#  示例 2:
#
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
#  说明:
#
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#  Related Topics 双指针 字符串
#  👍 502 👎 0

"""

# Rabin Karp is OK
import pytest


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        lennd = len(needle)
        if not lennd:
            return 0
        for i in range(len(haystack) - lennd + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


class Solution1:
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        return self.KMP(haystack, needle)

    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        # print(prefix)
        for i in range(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getPrefix(self, pattern):
        lenP = len(pattern)
        prefixArray = [-1] * lenP
        j = -1
        for i in range(1, lenP):
            while j > -1 and pattern[j + 1] != pattern[i]:
                # print(i, j, pattern[j], prefixArray[j])
                j = prefixArray[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefixArray[i] = j
        return prefixArray


@pytest.mark.parametrize("kw,expected", [
    [dict(haystack="hello", needle="ll"), 2],
    [dict(haystack="aaaaa", needle="bba"), -1],
    [dict(haystack="helabalalaaballaalblacblaalaalalaabacbllalablaaao", needle="laalblacblaalaa"), 14],
])
def test_solutions(kw, expected):
    assert Solution().strStr(**kw) == expected
    assert Solution1().strStr(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
