#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 21:44:06
# @Last Modified : 2020-04-10 21:44:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



"""
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
#
#  示例 1：
#
#  输入: "the sky is blue"
# 输出: "blue is sky the"
#
#
#  示例 2：
#
#  输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
#
#  示例 3：
#
#  输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  说明：
#
#
#  无空格字符构成一个单词。
#  输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#  如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
#  进阶：
#
#  请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
#  Related Topics 字符串
#  👍 198 👎 0

"""

import os
import sys
import traceback

import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))




@pytest.mark.parametrize("args,expected", [
    ("the sky is blue", "blue is sky the"),
    ("  hello world!  ", "world! hello"),
    ("a good   example", "example good a"),
])
def test_solutions(args, expected):
    assert Solution().reverseWords(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

























