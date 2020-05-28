#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  示例 1: 
# 
#  输入: "hello"
# 输出: "holle"
#  
# 
#  示例 2: 
# 
#  输入: "leetcode"
# 输出: "leotcede" 
# 
#  说明: 
# 元音字母不包含字母"y"。 
#  Related Topics 双指针 字符串

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        need_trans="aeiouAEIOU"
        chars = list(s)
        l,r=0,len(chars)-1
        while l<r:
            while l<r and chars[l] not in need_trans:
                l+=1
            while  l<r and chars[r] not in need_trans:
                r-=1
            chars[l],chars[r]=chars[r],chars[l]
            l+=1
            r-=1
        return "".join(chars)

        
# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("hello", "holle"),
    pytest.param("leetcode", "leotcede" ),
])
def test_solutions(args, expected):
    assert Solution().reverseVowels(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])