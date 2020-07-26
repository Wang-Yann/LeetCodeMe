#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-24 10:38:22
# @Last Modified : 2020-07-24 10:38:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 为搜索引擎设计一个搜索自动补全系统。用户会输入一条语句（最少包含一个字母，以特殊字符 '#' 结尾）。除 '#' 以外用户输入的每个字符，返回历史中热度前三
# 并以当前输入部分为前缀的句子。下面是详细规则： 
# 
#  
#  一条句子的热度定义为历史上用户输入这个句子的总次数。 
#  返回前三的句子需要按照热度从高到低排序（第一个是最热门的）。如果有多条热度相同的句子，请按照 ASCII 码的顺序输出（ASCII 码越小排名越前）。 
#  如果满足条件的句子个数少于 3，将它们全部输出。 
#  如果输入了特殊字符，意味着句子结束了，请返回一个空集合。 
#  
# 
#  你的工作是实现以下功能： 
# 
#  构造函数： 
# 
#  AutocompleteSystem(String[] sentences, int[] times): 这是构造函数，输入的是历史数据。 Sentenc
# es 是之前输入过的所有句子，Times 是每条句子输入的次数，你的系统需要记录这些历史信息。 
# 
#  现在，用户输入一条新的句子，下面的函数会提供用户输入的下一个字符： 
# 
#  List<String> input(char c): 其中 c 是用户输入的下一个字符。字符只会是小写英文字母（'a' 到 'z' ），空格（' '）和
# 特殊字符（'#'）。输出历史热度前三的具有相同前缀的句子。 
# 
#  
# 
#  样例 ： 
# 操作 ： AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"],
#  [5,3,2,2]) 
# 系统记录下所有的句子和出现的次数： 
# "i love you" : 5 次 
# "island" : 3 次 
# "ironman" : 2 次 
# "i love leetcode" : 2 次 
# 现在，用户开始新的键入： 
# 
#  
# 输入 ： input('i') 
# 输出 ： ["i love you", "island","i love leetcode"] 
# 解释 ： 
# 有四个句子含有前缀 "i"。其中 "ironman" 和 "i love leetcode" 有相同的热度，由于 ' ' 的 ASCII 码是 32 而 '
# r' 的 ASCII 码是 114，所以 "i love leetcode" 在 "ironman" 前面。同时我们只输出前三的句子，所以 "ironman" 
# 被舍弃。 
#  
# 输入 ： input(' ') 
# 输出 ： ["i love you","i love leetcode"] 
# 解释: 
# 只有两个句子含有前缀 "i "。 
#  
# 输入 ： input('a') 
# 输出 ： [] 
# 解释 ： 
# 没有句子有前缀 "i a"。 
#  
# 输入 ： input('#') 
# 输出 ： [] 
# 解释 ： 
# 
#  用户输入结束，"i a" 被存到系统中，后面的输入被认为是下一次搜索。 
# 
#  
# 
#  注释 ： 
# 
#  
#  输入的句子以字母开头，以 '#' 结尾，两个字母之间最多只会出现一个空格。 
#  即将搜索的句子总数不会超过 100。每条句子的长度（包括已经搜索的和即将搜索的）也不会超过 100。 
#  即使只有一个字母，输出的时候请使用双引号而不是单引号。 
#  请记住清零 AutocompleteSystem 类中的变量，因为静态变量、类变量会在多组测试数据中保存之前结果。详情请看这里。 
#  
# 
#  
#  Related Topics 设计 字典树 
#  👍 33 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class TrieNode(object):

    def __init__(self):
        self.children = dict()
        self.sentences = set()


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.buffer = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.cur = self.trie

    def input(self, c):

        ans = []
        if c != '#':
            self.buffer += c
            if self.cur:
                self.cur = self.cur.children.get(c)
            if self.cur:
                ans = sorted(self.cur.sentences, key=lambda x: (-self.stimes[x], x))[:3]

        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.cur = self.trie
        return ans

    def addSentence(self, sentence):
        cur = self.trie
        for letter in sentence:
            child = cur.children.get(letter)
            if child is None:
                child = TrieNode()
                cur.children[letter] = child
            cur = child
            child.sentences.add(sentence)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    assert obj.input("i") == ["i love you", "island", "i love leetcode"]
    assert obj.input(" ") == ["i love you", "i love leetcode"]
    assert obj.input("a") == []
    assert obj.input("#") == []


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
