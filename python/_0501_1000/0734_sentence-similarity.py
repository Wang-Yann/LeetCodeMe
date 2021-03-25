#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 11:57:45
# @Last Modified : 2020-07-31 11:57:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。 
# 
#  例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"
# ]]的时候，"great acting skills" 和 "fine drama talent" 是相似的。 
# 
#  注意相似关系是不具有传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，但是 "great" 和 
# "good" 未必是相似的。 
# 
#  但是，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。 
# 
#  而且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = [] 是相似的
# ，尽管没有输入特定的相似单词对。 
# 
#  最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 = ["double
# plus","good"] 相似。 
# 
#  
# 
#  注： 
# 
#  
#  words1 and words2 的长度不会超过 1000。 
#  pairs 的长度不会超过 2000。 
#  每个pairs[i] 的长度为 2。 
#  每个 words[i] 和 pairs[i][j] 的长度范围为 [1, 20]。 
#  
# 
#  
#  Related Topics 哈希表 
#  👍 14 👎 0

"""
import collections
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        lookup = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in lookup or (w2, w1) in lookup for w1, w2 in zip(words1, words2))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        # if len(words1)!=len(words2):
        #     return False
        lookup = collections.defaultdict(set)
        for p1, p2 in pairs:
            lookup[p1].add(p2)
        for a, b in itertools.zip_longest(words1, words2, fillvalue=''):
            if not (a == b or b in lookup[a] or a in lookup[b]):
                return False
        return True


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

    [dict(
        words1=["this", "summer", "thomas", "get", "actually", "actually", "rich", "and", "possess", "the", "actually",
                "great", "and", "fine", "vehicle", "every", "morning", "he", "drives", "one", "nice", "car", "around",
                "one", "great", "city", "to", "have", "single", "super", "excellent", "super", "as", "his", "brunch",
                "but", "he", "only", "eat", "single", "few", "fine", "food", "as", "some", "fruits", "he", "wants",
                "to", "eat", "an", "unique", "and", "actually", "healthy", "life"],
        words2=["this", "summer", "thomas", "get", "very", "very", "rich", "and", "possess", "the", "very", "fine",
                "and", "well", "car", "every", "morning", "he", "drives", "a", "fine", "car", "around", "unique",
                "great", "city", "to", "take", "any", "really", "wonderful", "fruits", "as", "his", "breakfast", "but",
                "he", "only", "drink", "an", "few", "excellent", "breakfast", "as", "a", "super", "he", "wants", "to",
                "drink", "the", "some", "and", "extremely", "healthy", "life"],
        pairs=[["good", "nice"], ["good", "excellent"], ["good", "well"], ["good", "great"], ["fine", "nice"],
               ["fine", "excellent"], ["fine", "well"], ["fine", "great"], ["wonderful", "nice"],
               ["wonderful", "excellent"], ["wonderful", "well"], ["wonderful", "great"], ["extraordinary", "nice"],
               ["extraordinary", "excellent"], ["extraordinary", "well"], ["extraordinary", "great"], ["one", "a"],
               ["one", "an"], ["one", "unique"], ["one", "any"], ["single", "a"], ["single", "an"],
               ["single", "unique"], ["single", "any"], ["the", "a"], ["the", "an"], ["the", "unique"], ["the", "any"],
               ["some", "a"], ["some", "an"], ["some", "unique"], ["some", "any"], ["car", "vehicle"],
               ["car", "automobile"], ["car", "truck"], ["auto", "vehicle"], ["auto", "automobile"], ["auto", "truck"],
               ["wagon", "vehicle"], ["wagon", "automobile"], ["wagon", "truck"], ["have", "take"], ["have", "drink"],
               ["eat", "take"], ["eat", "drink"], ["entertain", "take"], ["entertain", "drink"], ["meal", "lunch"],
               ["meal", "dinner"], ["meal", "breakfast"], ["meal", "fruits"], ["super", "lunch"], ["super", "dinner"],
               ["super", "breakfast"], ["super", "fruits"], ["food", "lunch"], ["food", "dinner"],
               ["food", "breakfast"], ["food", "fruits"], ["brunch", "lunch"], ["brunch", "dinner"],
               ["brunch", "breakfast"], ["brunch", "fruits"], ["own", "have"], ["own", "possess"], ["keep", "have"],
               ["keep", "possess"], ["very", "super"], ["very", "actually"], ["really", "super"],
               ["really", "actually"], ["extremely", "super"], ["extremely", "actually"]]

    ), True],
])
def test_solutions(kw, expected):
    assert Solution().areSentencesSimilar(**kw) == expected
    assert Solution1().areSentencesSimilar(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
