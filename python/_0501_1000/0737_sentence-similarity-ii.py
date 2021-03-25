#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 12:01:19
# @Last Modified : 2020-07-31 12:01:19
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。 
# 
#  例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"
# ]]的时候，words1 = ["great", "acting", "skills"] 和 words2 = ["fine", "drama", "talen
# t"] 是相似的。 
# 
#  注意相似关系是 具有 传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，则 "great" 和 
# "good" 是相似的。 
# 
#  而且，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。 
# 
#  并且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = [] 是相似的
# ，尽管没有输入特定的相似单词对。 
# 
#  最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 = ["double
# plus","good"] 相似。 
# 
#  注： 
# 
#  
#  words1 and words2 的长度不会超过 1000。 
#  pairs 的长度不会超过 2000。 
#  每个pairs[i] 的长度为 2。 
#  每个 words[i] 和 pairs[i][j] 的长度范围为 [1, 20]。 
#  
#  Related Topics 深度优先搜索 并查集 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, max_size):
        self.set = list(range(max_size))

    def find_set(self, x):
        if x != self.set[x]:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """AC"""
        if len(words1) != len(words2):
            return False
        all_words = {x for pair in pairs for x in pair}
        lookup = dict(zip(all_words, range(len(all_words))))
        uf = UnionFind(len(all_words))
        for x, y in pairs:
            uf.union_set(lookup[x], lookup[y])
        for a, b in zip(words1, words2):
            if a == b:
                continue
            if not (a in lookup and b in lookup and uf.find_set(lookup[a]) == uf.find_set(lookup[b])):
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        pairs=[["great", "fine"], ["acting", "drama"], ["skills", "talent"]],
        words1=["great", "acting", "skills"],
        words2=["fine", "drama", "talent"]
    ), True],
    [dict(
        words1=["great"], words2=["great"], pairs=[]
    ), True],
    [dict(
        words1=["great"], words2=["double", "plus", "good"],
        pairs=[["great", "fine"], ["acting", "drama"], ["skills", "talent"]]
    ), False],
])
def test_solutions(kw, expected):
    assert Solution().areSentencesSimilarTwo(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
