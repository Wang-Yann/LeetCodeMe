#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 17:12:28
# @Last Modified : 2020-07-22 17:12:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。 
# 
#  示例 1： 
# 
#  输入: "code"
# 输出: false 
# 
#  示例 2： 
# 
#  输入: "aab"
# 输出: true 
# 
#  示例 3： 
# 
#  输入: "carerac"
# 输出: true 
#  Related Topics 哈希表 
#  👍 19 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """AC"""
        counter = collections.Counter(s)
        return sum(v % 2 for v in counter.values()) <= 1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("code", False),
    ("aab", True),
    ("carerac", True),
])
def test_solutions(args, expected):
    assert Solution().canPermutePalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
