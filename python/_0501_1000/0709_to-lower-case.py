#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: "Hello"
# 输出: "hello" 
# 
#  示例 2： 
# 
#  
# 输入: "here"
# 输出: "here" 
# 
#  示例 3： 
# 
#  
# 输入: "LOVELY"
# 输出: "lovely"
#  
#  Related Topics 字符串

"""
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def toLowerCase(self, str: str) -> str:
        delta = ord("a") - ord("A")
        ans = ""
        for char in str:
            if char in string.ascii_uppercase:
                ans += chr(ord(char) + delta)
            else:
                ans += char
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("Hello", "hello"),
    ("here", "here"),
    ("LOVELY", "lovely"),
])
def test_solutions(args, expected):
    assert Solution().toLowerCase(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
