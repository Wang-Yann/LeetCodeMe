#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 09:41:02
# @Last Modified : 2020-04-26 09:41:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#
#
#  示例 1:
#
#  输入: "bcabc"
# 输出: "abc"
#
#
#  示例 2:
#
#  输入: "cbacdcbc"
# 输出: "acdb"
#
#
#
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同
#  Related Topics 栈 贪心算法
#  👍 185 👎 0
import collections

import pytest


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Good"""
        in_stack = set()
        remaining = collections.Counter(s)
        stack = []
        for char in s:
            if char not in in_stack:
                while stack and stack[-1] > char and remaining[stack[-1]] > 0:
                    in_stack.remove(stack.pop())
                stack.append(char)
                in_stack.add(char)
            remaining[char] -= 1
        return "".join(stack)


@pytest.mark.parametrize("args,expected", [
    ("cdadabcc", "adbc"),
    ("abcd", "abcd"),
    ("ecbacba", "eacb"),
    ("leetcode", "letcod"),
])
def test_solutions(args, expected):
    assert Solution().removeDuplicateLetters(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
