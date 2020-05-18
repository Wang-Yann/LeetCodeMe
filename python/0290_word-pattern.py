#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  示例1: 
# 
#  输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false 
# 
#  示例 4: 
# 
#  输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false 
# 
#  说明: 
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
#  Related Topics 哈希表

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        ch2w,w2ch ={},{}
        if len(words)!=len(pattern):
            return False
        for char,word in zip(pattern,words):
            if char not  in ch2w and word not in w2ch:
                ch2w[char]=word
                w2ch[word]=char
            elif  char not in ch2w or ch2w[char]!=word:
                return False

        return True


        
# leetcode submit region end(Prohibit modification and deletion)



@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        pattern = "abba", str = "dog cat cat dog"
    ), True),
    pytest.param(dict( pattern = "abba", str = "dog cat cat fish"  ), False),
    pytest.param(dict( pattern = "aaaa", str = "dog cat cat dog"  ), False),
    pytest.param(dict( pattern = "abba", str = "dog dog dog dog"  ), False),
    pytest.param(dict( pattern = "abb", str = "cat dog dog dog"  ), False),
])
def test_solutions(kwargs, expected):
    assert Solution().wordPattern(**kwargs) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])