#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 13:42:01
# @Last Modified : 2020-07-27 13:42:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。 
# 
#  以下是一些单词缩写的范例： 
# 
#  a) it                      --> it    (没有缩写)
# 
#      1
#      ↓
# b) d|o|g                   --> d1g
# 
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
#  
# 
#  请你判断单词缩写在字典中是否唯一。当单词的缩写满足下面任何一个条件是，可以认为该单词缩写是唯一的： 
# 
#  
#  字典 dictionary 中没有任何其他单词的缩写与该单词 word 的缩写相同。 
#  字典 dictionary 中的所有缩写与该单词 word 的缩写相同的单词都与 word 相同。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：
# ["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
# [[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]
# 输出：
# [null,false,true,false,true]
# 
# 解释：
# ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card
# "]);
# validWordAbbr.isUnique("dear"); // return False
# validWordAbbr.isUnique("cart"); // return True
# validWordAbbr.isUnique("cane"); // return False
# validWordAbbr.isUnique("make"); // return True
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个单词都只由小写字符组成 
#  
#  Related Topics 设计 哈希表 
#  👍 3 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class ValidWordAbbr:
    """AC"""

    def __init__(self, dictionary: List[str]):
        self.lookup = collections.defaultdict(set)
        for word in dictionary:
            if len(word) > 2:
                k = word[0] + str(len(word) - 2) + word[-1]
                self.lookup[k].add(word)

    def isUnique(self, word: str) -> bool:
        if len(word) > 2:
            k = word[0] + str(len(word) - 2) + word[-1]
        else:
            k = len(word)
        if self.lookup[k] in (set(), {word}):
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    validWordAbbr = ValidWordAbbr(["deer", "door", "cake", "card"])
    assert validWordAbbr.isUnique("dear") == False
    assert validWordAbbr.isUnique("cart") == True
    assert validWordAbbr.isUnique("cane") == False
    assert validWordAbbr.isUnique("make") == True


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
