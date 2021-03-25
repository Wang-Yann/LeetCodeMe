#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:44:50
# @Last Modified : 2020-07-06 23:44:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。 
# 
#  请你返回结果字符串。如果无法做到，则返回一个空串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：palindrome = "abccba"
# 输出："aaccba"
#  
# 
#  示例 2： 
# 
#  输入：palindrome = "a"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= palindrome.length <= 1000 
#  palindrome 只包含小写英文字母。 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def breakPalindrome(self, palindrome: str) -> str:
        """
        Check half of the string,
        replace a non 'a' character to 'a'.

        If only one character, return empty string.
        Otherwise replace the last character to 'b'
        """
        chars = list(palindrome)
        for i in range(len(chars) // 2):
            if chars[i] != "a":
                chars[i] = "a"
                return "".join(chars)
        return palindrome[:-1] + "b" if len(palindrome) >= 2 else ""


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(palindrome="abccba"), "aaccba"),
    pytest.param(dict(palindrome="a"), ""),
    pytest.param(dict(palindrome="aa"), "ab"),
    pytest.param(dict(palindrome="aba"), "abb"),
])
def test_solutions(kwargs, expected):
    assert Solution().breakPalindrome(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
