#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定多个 words，words[i] 的权重为 i 。 
# 
#  设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。这个函数将返回具有前缀 p
# refix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。 
# 
#  例子: 
# 
#  
# 输入:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // 返回 0
# WordFilter.f("b", "") // 返回 -1
#  
# 
#  注意: 
# 
#  
#  words的长度在[1, 15000]之间。 
#  对于每个测试用例，最多会有words.length次对WordFilter.f的调用。 
#  words[i]的长度在[1, 10]之间。 
#  prefix, suffix的长度在[0, 10]之前。 
#  words[i]和prefix, suffix只包含小写字母。 
#  
#  Related Topics 字典树

"""
import collections
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
Trie = lambda: collections.defaultdict(Trie)


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for weight, word in enumerate(words):
            word += "#"
            length = len(word)
            for i in range(length):
                cur = self.trie
                cur["_weight"] = weight
                for j in range(i, 2 * length - 1):
                    cur = cur[word[j % length]]
                    cur["_weight"] = weight

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + "#" + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]

        return cur["_weight"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# leetcode submit region end(Prohibit modification and deletion)

def test_design():
    obj = WordFilter(["apple","hello"])
    assert obj.f("a", "e") == 0  # 返回 0
    assert obj.f("b", "") == -1  # 返回 -1
    assert obj.f("he", "o") == 1  # 返回 -1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
