#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个支持以下两种操作的数据结构： 
# 
#  void addWord(word)
# bool search(word)
#  
# 
#  search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。 
# 
#  示例: 
# 
#  addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#  
# 
#  说明: 
# 
#  你可以假设所有单词都是由小写字母 a-z 组成的。 
#  Related Topics 设计 字典树 回溯算法

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class TrieNode(object):

    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            if char not in cur.leaves:
                cur.leaves[char] = TrieNode()
            cur = cur.leaves[char]
        cur.is_string = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def helper(start, cur):
            if start == len(word):
                return cur.is_string
            if word[start] in cur.leaves:
                return helper(start + 1, cur.leaves[word[start]])
            elif word[start] == ".":
                for char in cur.leaves:
                    if helper(start + 1, cur.leaves[char]):
                        return True
            return False

        return helper(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    assert not obj.search("pad")
    assert obj.search("bad")
    assert obj.search(".ad")
    assert obj.search("b..")


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
