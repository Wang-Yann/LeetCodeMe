#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 实现一个带有buildDict, 以及 search方法的魔法字典。 
# 
#  对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。 
# 
#  对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。 
# 
#  示例 1: 
# 
#  
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#  
# 
#  注意: 
# 
#  
#  你可以假设所有输入都是小写字母 a-z。 
#  为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。 
#  请记住重置MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅这里了解更多详情。 
#  
#  Related Topics 字典树 哈希表

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.count = collections.Counter()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.words.add(word)
            self.count.update(nei for nei in self._generate_neighbors(word))

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._generate_neighbors(word))

    def _generate_neighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i + 1:]


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    # print(obj.count)
    assert obj.search("hello") == False
    assert obj.search("hhllo") == True
    assert obj.search("hell") == False
    assert obj.search("leetcoded") == False


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
