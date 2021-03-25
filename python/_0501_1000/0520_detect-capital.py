#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个单词，你需要判断单词的大写使用是否正确。 
# 
#  我们定义，在以下情况时，单词的大写用法是正确的： 
# 
#  
#  全部字母都是大写，比如"USA"。 
#  单词中所有字母都不是大写，比如"leetcode"。 
#  如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。 
#  
# 
#  否则，我们定义这个单词没有正确使用大写字母。 
# 
#  示例 1: 
# 
#  
# 输入: "USA"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "FlaG"
# 输出: False
#  
# 
#  注意: 输入是由大写和小写拉丁字母组成的非空单词。 
#  Related Topics 字符串

"""
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def detectCapitalUse(self, word: str) -> bool:
        if all(char in string.ascii_uppercase for char in word):
            return True
        for char in word[1:]:
            if char.isupper():
                return False
        return True


@pytest.mark.parametrize("args,expected", [
    ("USA", True),
    pytest.param("FlaG", False),
])
def test_solutions(args, expected):
    assert Solution().detectCapitalUse(args) == expected
    assert Solution1().detectCapitalUse(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
