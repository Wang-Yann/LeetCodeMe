#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 16:35:16
# @Last Modified : 2020-04-30 16:35:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
#  你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
#
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。
#
#  示例 1:
# s = "abc", t = "ahbgdc"
#
#  返回 true.
#
#  示例 2:
# s = "axc", t = "ahbgdc"
#
#  返回 false.
#
#  后续挑战 :
#
#  如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码
# ？
#
#  致谢:
#
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#  Related Topics 贪心算法 二分查找 动态规划
#  👍 222 👎 0

"""

import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        for char in t:
            if char == s[i]:
                i += 1
            if i == len(s):
                return True
        return i == len(s)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abc", t="ahbgdc"), True],
    [dict(s="axc", t="ahbgdc"), False],
])
def test_solutions(kw, expected):
    assert Solution().isSubsequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
