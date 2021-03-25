#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符： 
# 
#  
#  字符（'a' - 'i'）分别用（'1' - '9'）表示。 
#  字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
#  
# 
#  返回映射之后形成的新字符串。 
# 
#  题目数据保证映射始终唯一。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "10#11#12"
# 输出："jkab"
# 解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
#  
# 
#  示例 2： 
# 
#  输入：s = "1326#"
# 输出："acz"
#  
# 
#  示例 3： 
# 
#  输入：s = "25#"
# 输出："y"
#  
# 
#  示例 4： 
# 
#  输入：s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# 输出："abcdefghijklmnopqrstuvwxyz"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] 只包含数字（'0'-'9'）和 '#' 字符。 
#  s 是映射始终存在的有效字符串。 
#  
#  Related Topics 字符串

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def freqAlphabets(self, s):
       

        def alpha(num):
            return chr(ord('a') + int(num) - 1)

        i = len(s) - 1
        result = []
        while i >= 0:
            if s[i] == '#':
                result.append(alpha(s[i - 2:i]))
                i -= 3
            else:
                result.append(alpha(s[i]))
                i -= 1
        return "".join(reversed(result))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def freqAlphabets(self, s: str) -> str:
        lookup = {}
        for i in range(1, 27):
            if i >= 10:
                lookup["%d#" % i] = chr(ord("a") + i - 1)
            else:
                lookup["%d" % i] = chr(ord("a") + i - 1)
        ans = []
        i = 0
        N = len(s)
        while i < N:
            if '3' <= s[i] <= '9' or not s[i:i + 3].endswith("#"):
                ans.append(lookup[s[i]])
                i += 1
            else:
                ans.append(lookup[s[i:i + 3]])
                i += 3
        return "".join(ans)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="10#11#12"), "jkab"],
    [dict(s="1326#"), "acz"],
    [dict(s="25#"), "y"],
    [dict(s="12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"), "abcdefghijklmnopqrstuvwxyz"],
])
def test_solutions(kw, expected):
    assert Solution().freqAlphabets(**kw) == expected
    assert Solution1().freqAlphabets(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
