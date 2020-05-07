#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def _child_search(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._child_search(word)
        if node:
            return node.is_string
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._child_search(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    obj = Trie()
    obj.insert("hello")
    obj.insert("helen")
    assert not obj.search("word")
    assert  obj.search("hello")
    assert obj.startsWith("he")


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
