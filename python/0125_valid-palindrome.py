#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1

        return True


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


@pytest.mark.parametrize("args,expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False)
])
def test_solutions(args, expected):
    assert Solution().isPalindrome(args) == expected
    assert Solution1().isPalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
