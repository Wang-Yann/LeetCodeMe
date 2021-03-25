#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。 
# 
#  给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：text = "ababa"
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：text = "aaabaaa"
# 输出：6
#  
# 
#  示例 3： 
# 
#  输入：text = "aaabbaaa"
# 输出：4
#  
# 
#  示例 4： 
# 
#  输入：text = "aaaaa"
# 输出：5
#  
# 
#  示例 5： 
# 
#  输入：text = "abcdef"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 20000 
#  text 仅由小写英文字母组成。 
#  
#  Related Topics 字符串

"""

import collections
import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxRepOpt1(self, text: str) -> int:
        # We get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
        A = [(char, len(list(group))) for char, group in itertools.groupby(text)]
        # We also generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
        counter = collections.Counter(text)
        # only extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, counter[char]) for char, k in A)
        # merge 2 groups together
        for i in range(1, len(A) - 1):
            # if both sides have the same char and are separated by only 1 char
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                # min here serves the same purpose
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, counter[A[i + 1][0]]))
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(text="ababa"), 3),
    pytest.param(dict(text="aaabaaa"), 6),
    pytest.param(dict(text="aaabbaaa"), 4),
    pytest.param(dict(text="aaaaa"), 5),
    pytest.param(dict(text="abcdef"), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().maxRepOpt1(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
