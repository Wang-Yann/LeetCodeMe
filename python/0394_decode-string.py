#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:57:44
# @Last Modified : 2020-04-26 10:57:44
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
#  示例 1：
#
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
#  示例 2：
#
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
#  示例 3：
#
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
#  示例 4：
#
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#  Related Topics 栈 深度优先搜索
#  👍 415 👎 0

"""

import pytest


class Solution0:
    def decodeString(self, s: str) -> str:
        """
        TODO
        """
        stack, res, times = [], "", 0
        for c in s:
            if c == "[":
                stack.append([times, res])
                res, times = "", 0
            elif c == "]":
                cur_times, last_res = stack.pop()
                res = last_res + cur_times * res
            elif "0" <= c <= "9":
                times = times * 10 + ord(c) - ord("0")
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        times_stack = []
        str_stack = []

        num, cur = 0, ""
        i = 0
        length = len(s)
        while i <= length - 1:
            if s[i] == "[":
                times_stack.append(num)
                str_stack.append(cur)
                num = 0
                cur = ""
                i += 1
            elif s[i].isalpha():
                j = i + 1
                while j <= length - 1 and s[j].isalpha():
                    j += 1
                cur += s[i:j]
                i = j
            elif s[i].isdigit():
                j = i + 1
                while j <= length - 1 and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j
            elif s[i] == "]":
                times = times_stack.pop()
                last = str_stack.pop()
                cur = last + cur * times
                i += 1
        return cur


@pytest.mark.parametrize("args,expected", [
    ("3[a]2[b4[F]c]", "aaabFFFFcbFFFFc"),
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("3[a2[c1[ee]]]", "aceeceeaceeceeaceecee"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
])
def test_solutions(args, expected):
    assert Solution0().decodeString(args) == expected
    assert Solution().decodeString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
