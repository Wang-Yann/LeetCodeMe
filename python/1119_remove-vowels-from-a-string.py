#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:06:20
# @Last Modified : 2020-08-04 17:06:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："leetcodeisacommunityforcoders"
# 输出："ltcdscmmntyfrcdrs"
#  
# 
#  示例 2： 
# 
#  输入："aeiou"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 仅由小写英文字母组成。 
#  1 <= S.length <= 1000 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""
import re

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeVowels(self, S: str) -> str:
        return re.sub(r"[aeiou]+", "", S)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs"),
    ("aeiou", ""),
])
def test_solutions(args, expected):
    assert Solution().removeVowels(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
