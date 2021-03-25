#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 17:33:52
# @Last Modified : 2020-07-21 17:33:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串，逐个翻转字符串中的每个单词。 
# 
#  示例： 
# 
#  输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"] 
# 
#  注意： 
# 
#  
#  单词的定义是不包含空格的一系列字符 
#  输入字符串中不会包含前置或尾随的空格 
#  单词与单词之间永远是以单个空格隔开的 
#  
# 
#  进阶：使用 O(1) 额外空间复杂度的原地解法。 
#  Related Topics 字符串 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        GOOD
        Do not return anything, modify s in-place instead.
        """

        def reverseRange(begin, end):
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        N = len(s)
        i = 0
        reverseRange(0, N)
        for j in range(N + 1):
            if j == N or s[j] == " ":
                reverseRange(i, j)
                i = j + 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"],
     ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"])
])
def test_solutions(args, expected):
    Solution().reverseWords(args)
    assert args == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
