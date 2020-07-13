#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:51:21
# @Last Modified : 2020-07-13 14:51:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个方法，找出任意指定单词在一本书中的出现频率。 
# 
#  你的实现应该支持如下操作： 
# 
#  
#  WordsFrequency(book)构造函数，参数为字符串数组构成的一本书 
#  get(word)查询指定单词在书中出现的频率 
#  
# 
#  示例： 
# 
#  WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple
# ", "he", "have", "a", "pen"});
# wordsFrequency.get("you"); //返回0，"you"没有出现过
# wordsFrequency.get("have"); //返回2，"have"出现2次
# wordsFrequency.get("an"); //返回1
# wordsFrequency.get("apple"); //返回1
# wordsFrequency.get("pen"); //返回1
#  
# 
#  提示： 
# 
#  
#  book[i]中只包含小写字母 
#  1 <= book.length <= 100000 
#  1 <= book[i].length <= 10 
#  get函数的调用次数不会超过100000 
#  
#  Related Topics 设计 哈希表 
#  👍 7 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.counter = collections.Counter(book)

    def get(self, word: str) -> int:
        return self.counter[word]


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    wordsFrequency = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    assert wordsFrequency.get("you") == 0
    assert wordsFrequency.get("have") == 2
    assert wordsFrequency.get("an") == 1
    assert wordsFrequency.get("apple") == 1
    assert wordsFrequency.get("pen") == 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
