#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 18:20:46
# @Last Modified : 2020-07-21 18:20:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和 word2，并返回列表中这两个单词之间的
# 最短距离。您的方法将被以不同的参数调用 多次。 
# 
#  示例: 
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"] 
# 
#  输入: word1 = "coding”, word2 = "practice”
# 输出: 3
#  
# 
#  输入: word1 = "makes", word2 = "coding"
# 输出: 1 
# 
#  注意: 
# 你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。 
#  Related Topics 设计 哈希表 
#  👍 16 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class WordDistance:

    def __init__(self, words: List[str]):
        self.lookup = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.lookup[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        idx1, idx2 = self.lookup[word1], self.lookup[word2]
        i = j = 0
        ans = 0x7fffffff
        while i < len(idx1) and j < len(idx2):
            ans = min(ans, abs(idx1[i] - idx2[j]))
            if idx1[i] < idx2[j]:
                i += 1
            else:
                j += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    sol = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    assert sol.shortest(word1="coding", word2="practice") == 3
    assert sol.shortest(word1="makes", word2="coding") == 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
