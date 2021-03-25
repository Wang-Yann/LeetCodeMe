#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。 
# 
#  示例 1: 
# 
#  
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
#  
# 
#  注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。 
#  Related Topics 字符串

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reverseWords(self, s: str) -> str:
        reversed_words = [word[::-1] for word in s.split(" ")]
        return " ".join(reversed_words)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def reverseWords(self, s: str) -> str:
        chars = list(s)
        length = len(chars)
        i = 0
        while i <= length - 1:
            if chars[i].isspace():
                i += 1
                continue
            j = i
            while j <= length - 1 and not chars[j].isspace():
                j += 1
            chars[i:j] = chars[i:j][::-1]
            i = j
        return "".join(chars)


@pytest.mark.parametrize("args,expected", [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    (" hello  ll", " olleh  ll"),
    (" ", " "),
])
def test_solutions(args, expected):
    assert Solution().reverseWords(args) == expected
    assert Solution1().reverseWords(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
