#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个产品数组 products 和一个字符串 searchWord ，products 数组中每个产品都是一个字符串。 
# 
#  请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品
# 。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。 
# 
#  请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord 
# = "mouse"
# 输出：[
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# 解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
# 输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
# 输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
#  
# 
#  示例 2： 
# 
#  输入：products = ["havana"], searchWord = "havana"
# 输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#  
# 
#  示例 3： 
# 
#  输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# 
# 输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"]
# ,["bags"]]
#  
# 
#  示例 4： 
# 
#  输入：products = ["havana"], searchWord = "tatiana"
# 输出：[[],[],[],[],[],[],[]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= products.length <= 1000 
#  1 <= Σ products[i].length <= 2 * 10^4 
#  products[i] 中所有的字符都是小写英文字母。 
#  1 <= searchWord.length <= 1000 
#  searchWord 中所有字符都是小写英文字母。 
#  
#  Related Topics 字符串

"""
import bisect
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class TrieNode(object):

    def __init__(self):
        self.__TOP_COUNT = 3
        self.leaves = collections.defaultdict(TrieNode)
        self.infos = []

    def insert(self, words, i):
        curr = self
        for c in words[i]:
            curr = curr.leaves[c]
            curr.add_info(words, i)

    def add_info(self, words, i):
        self.infos.append(i)
        self.infos.sort(key=lambda x: words[x])
        if len(self.infos) > self.__TOP_COUNT:
            self.infos.pop()


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = TrieNode()
        for i in range(len(products)):
            trie.insert(products, i)
        res = [[] for _ in range(len(searchWord))]
        for i, char in enumerate(searchWord):
            if char not in trie.leaves:
                break
            trie = trie.leaves[char]
            res[i] = list(map(lambda x: products[x], trie.infos))
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        if A[i] is a prefix of A[j], A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]
        """
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"),
     [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
      ["mouse", "mousepad"], ["mouse", "mousepad"]]],
    [dict(products=["havana"], searchWord="havana"),
     [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
     ],
    [dict(products=["bags", "baggage", "banner", "box", "cloths"], searchWord="bags"),
     [["baggage", "bags", "banner"], ["baggage", "bags", "banner"], ["baggage", "bags"], ["bags"]]
     ],
    [dict(products=["havana"], searchWord="tatiana"),
     [[], [], [], [], [], [], []]
     ],
])
def test_solutions(kw, expected):
    assert Solution().suggestedProducts(**kw) == expected
    assert Solution1().suggestedProducts(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
