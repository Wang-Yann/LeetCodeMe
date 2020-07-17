#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 22:45:44
# @Last Modified : 2020-05-01 22:45:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符
# 串。如果答案不存在，则返回空字符串。
#
#  示例 1:
#
#
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# 输出:
# "apple"
#
#
#  示例 2:
#
#
# 输入:
# s = "abpcplea", d = ["a","b","c"]
#
# 输出:
# "a"
#
#
#  说明:
#
#
#  所有输入的字符串只包含小写字母。
#  字典的大小不会超过 1000。
#  所有输入的字符串长度不会超过 1000。
#
#  Related Topics 排序 双指针
#  👍 78 👎 0

from typing import List

import pytest


class Solution:

    def findLongestWord(self, s: str, d: List[str]) -> str:
        """GOOD"""
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            if i == len(word):
                return word
        return ""


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="abpcplea", d=["ale", "apple", "monkey", "plea"]), "apple"),
    pytest.param(dict(s="abpcplea", d=["a", "b", "c"]), "a"),
])
def test_solutions(kwargs, expected):
    assert Solution().findLongestWord(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
