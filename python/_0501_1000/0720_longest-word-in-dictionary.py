#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返
# 回答案中字典序最小的单词。 
# 
#  若无答案，则返回空字符串。 
# 
#  示例 1: 
# 
#  
# 输入: 
# words = ["w","wo","wor","worl", "world"]
# 输出: "world"
# 解释: 
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出: "apple"
# 解释: 
# "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#  
# 
#  注意: 
# 
#  
#  所有输入的字符串都只包含小写字母。 
#  words数组长度范围为[1,1000]。 
#  words[i]的长度范围为[1,30]。 
#  
#  Related Topics 字典树 哈希表

"""

import collections
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
trie = lambda:collections.defaultdict(trie)


class Solution:

    def longestWord(self, words: List[str]) -> str:
        Trie = trie()
        for i, word in enumerate(words):
            cur = Trie
            for char in word:
                cur = cur[char]
            cur["_end"] = i
        stack = list(Trie.values())
        # print(stack)
        res = ""
        while stack:
            cur = stack.pop()
            # print([cur[letter] for letter in cur])
            if "_end" in cur:
                word = words[cur["_end"]]
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
                stack += [cur[letter] for letter in cur if letter != "_end"]
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):

    def longestWord(self, words):
        wordset = set(words)
        words.sort(key=lambda c:(-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""


@pytest.mark.parametrize("args,expected", [
    (["w", "wo", "wor", "worl", "world"], "world"),
    pytest.param(["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
])
def test_solutions(args, expected):
    assert Solution().longestWord(args) == expected
    assert Solution1().longestWord(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
