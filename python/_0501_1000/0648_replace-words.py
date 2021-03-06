#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，
# 跟随着单词 other(其他)，可以形成新的单词 another(另一个)。 
# 
#  现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。 
# 
#  你需要输出替换之后的句子。 
# 
#  
# 
#  示例： 
# 
#  输入：dict(词典) = ["cat", "bat", "rat"] sentence(句子) = "the cattle was rattled by
#  the battery"
# 输出："the cat was rat by the bat"
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入只包含小写字母。 
#  1 <= dict.length <= 1000 
#  1 <= dict[i].length <= 100 
#  1 <= 句中词语数 <= 1000 
#  1 <= 句中词语长度 <= 1000 
#  
#  Related Topics 字典树 哈希表

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class TrieNode(object):
    """
    前缀树
    """

    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dict:
            trie.insert(word)

        def replace(word):
            cur = trie
            for idx, char in enumerate(word):
                if char not in cur.leaves:
                    break
                cur = cur.leaves[char]
                if cur.is_string:
                    return word[:idx + 1]
            return word

        return " ".join(map(replace, sentence.split()))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(dict=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"),
     "the cat was rat by the bat"],
])
def test_solutions(kw, expected):
    assert Solution().replaceWords(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
