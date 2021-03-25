#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为
# 每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。 
# 
#  示例 1: 
# 
#  输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2: 
# 
#  输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。 
# 
#  示例 3: 
# 
#  输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。 
#  Related Topics 位运算

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxProduct(self, words: List[str]) -> int:
        length = len(words)
        if length <= 1:
            return 0
        words.sort(key=len, reverse=True)
        res = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                if set(words[j]) & set(words[i]):
                    continue
                if len(words[i] * len(words[j])) <= res:
                    break
                res = len(words[i]) * len(words[j])
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):
    """
    用一个二进制数来保存字符串中出现过的字母，二进制数的第i位是1，就表示这个字符串中出现过第i个英文


    """

    def maxProduct(self, words):
        """
        """
        sets = collections.Counter()
        for w in words:
            key = frozenset(w)
            sets[key] = max(sets[key], len(w))

        max_len = 0
        for x, vx in sets.items():
            for y, vy in sets.items():
                if not x.intersection(y):
                    max_len = max(max_len, vx * vy)
        return max_len


@pytest.mark.parametrize("args,expected", [
    (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
    (["a", "aa", "aaa", "aaaa"], 0),
    pytest.param(["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
])
def test_solutions(args, expected):
    assert Solution().maxProduct(args) == expected
    assert Solution1().maxProduct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
