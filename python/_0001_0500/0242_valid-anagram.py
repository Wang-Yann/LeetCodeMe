#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 20:32:22
# @Last Modified : 2020-05-01 20:32:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表
#  👍 217 👎 0

"""
import collections

import pytest


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution1(object):

    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)


@pytest.mark.parametrize("kw,expected", [
    (dict(s="anagram", t="nagaram"), True),
    pytest.param(dict(s="rat", t="car"), False),
])
def test_solutions(kw, expected):
    assert Solution().isAnagram(**kw) == expected
    assert Solution1().isAnagram(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
