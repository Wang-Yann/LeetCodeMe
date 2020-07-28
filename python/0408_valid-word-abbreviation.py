#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 16:46:06
# @Last Modified : 2020-07-28 16:46:06
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。 
# 
#  字符串 "word" 的所有有效缩写为： 
# 
#  ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
#  "w1r1", "1o2", "2r1", "3d", "w3", "4"] 
# 
#  注意单词 "word" 的所有有效缩写仅包含以上这些。任何其他的字符串都不是 "word" 的有效缩写。 
# 
#  注意: 
# 假设字符串 s 仅包含小写字母且 abbr 只包含小写字母和数字。 
# 
#  示例 1: 
# 
#  给定 s = "internationalization", abbr = "i12iz4n":
# 
# 函数返回 true.
#  
# 
#  
# 
#  示例 2: 
# 
#  给定 s = "apple", abbr = "a2e":
# 
# 函数返回 false.
#  
# 
#  
#  Related Topics 字符串 
#  👍 16 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        N = len(abbr)
        NW = len(word)
        abbrLen = num = 0
        for i in range(N):
            if abbr[i].isalpha():
                abbrLen += num + 1
                num = 0
                if abbrLen > NW or abbr[i] != word[abbrLen - 1]:
                    return False
            else:
                if not num and abbr[i] == "0":
                    return False
                num = num * 10 + int(abbr[i])
        return abbrLen + num == NW


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """AC"""
        NW, NA = len(word), len(abbr)
        i = j = 0
        while i < NW and j < NA:
            if not abbr[j].isdigit():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # "01 用例"
                if abbr[j] == "0":
                    return False
                cur_j = j
                while cur_j < NA and abbr[cur_j].isdigit():
                    cur_j += 1
                cnt = int(abbr[j:cur_j])
                j = cur_j
                i += cnt
        return i == NW and j == NA


@pytest.mark.parametrize("kw,expected", [
    [dict(word="internationalization", abbr="i12iz4n"), True],
    [dict(word="apple", abbr="a2e"), False],
    [dict(word="internationalization", abbr="i5a11o1"), True],
    [dict(word="a", abbr="01"), False],
])
def test_solutions(kw, expected):
    assert Solution().validWordAbbreviation(**kw) == expected
    assert Solution1().validWordAbbreviation(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
