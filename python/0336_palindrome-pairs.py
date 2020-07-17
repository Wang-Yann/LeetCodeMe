#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 22:18:24
# @Last Modified : 2020-05-03 22:18:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
#
#  示例 1:
#
#  输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]]
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
#  示例 2:
#
#  输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]]
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
#  Related Topics 字典树 哈希表 字符串
#  👍 76 👎 0

from typing import List

import pytest


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """HARD
        https://leetcode-cn.com/problems/palindrome-pairs/solution/hui-wen-dui-by-leetcode/
        """
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word:i for i, word in enumerate(words)}
        solutions = []
        for word_index, word in enumerate(words):
            reversed_word = word[::-1]
            # Build solutions of case #1. This word will be word 1.
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])

            # Build solutions of case #2. This word will be word 2.
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # Build solutions of case #3. This word will be word 1.
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])
        return solutions


@pytest.mark.parametrize("args,expected", [
    (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
    pytest.param(["bat", "tab", "cat"], [[0, 1], [1, 0]]),
])
def test_solutions(args, expected):
    assert Solution().palindromePairs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
