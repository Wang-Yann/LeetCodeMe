#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 18:39:48
# @Last Modified : 2020-07-22 18:39:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。 
# 
#  假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字
# 母顺序进行了排序。 
# 
#  您需要根据这个输入的列表，还原出此语言中已知的字母顺序。 
# 
#  
# 
#  示例 1： 
# 
#  输入:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# 输出: "wertf"
#  
# 
#  示例 2： 
# 
#  输入:
# [
#   "z",
#   "x"
# ]
# 输出: "zx"
#  
# 
#  示例 3： 
# 
#  输入:
# [
#   "z",
#   "x",
#   "z"
# ] 
# 输出: "" 
# 解释: 此顺序是非法的，因此返回 ""。
#  
# 
#  
# 
#  提示： 
# 
#  
#  你可以默认输入的全部都是小写字母 
#  若给定的顺序是不合法的，则返回空字符串即可 
#  若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可 
#  
#  Related Topics 图 拓扑排序 
#  👍 63 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    TODO
    BFS
    """

    def alienOrder(self, words: List[str]) -> str:
        result, in_degree, out_degree = [], collections.defaultdict(set), collections.defaultdict(set)
        zero_in_degree_queue = collections.deque()
        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in range(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and words[i - 1][:len(words[i])] == words[i]:
                return ""
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)
        # print(in_degree,out_degree,zero_in_degree_queue)
        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)

            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
                out_degree.pop(precedence)

        if out_degree:
            return ""

        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in range(str_len):
            if word1[i] != word2[i]:
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        words=[
            "wrt",
            "wrf",
            "er",
            "ett",
            "rftt"
        ]

    ), "wertf"],
    [dict(
        words=[
            "z",
            "x"
        ]
    ), "zx"],
    [dict(
        words=[
            "z",
            "x",
            "z"
        ]

    ), ""],
])
def test_solutions(kw, expected):
    assert Solution().alienOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
