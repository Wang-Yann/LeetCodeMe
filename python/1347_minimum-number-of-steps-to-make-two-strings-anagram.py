#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个长度相等的字符串 s 和 t。每一个步骤中，你可以选择将 t 中的 任一字符 替换为 另一个字符。 
# 
#  返回使 t 成为 s 的字母异位词的最小步骤数。 
# 
#  字母异位词 指字母相同，但排列不同（也可能相同）的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输出：s = "bab", t = "aba"
# 输出：1
# 提示：用 'b' 替换 t 中的第一个 'a'，t = "bba" 是 s 的一个字母异位词。
#  
# 
#  示例 2： 
# 
#  输出：s = "leetcode", t = "practice"
# 输出：5
# 提示：用合适的字符替换 t 中的 'p', 'r', 'a', 'i' 和 'c'，使 t 变成 s 的字母异位词。
#  
# 
#  示例 3： 
# 
#  输出：s = "anagram", t = "mangaar"
# 输出：0
# 提示："anagram" 和 "mangaar" 本身就是一组字母异位词。 
#  
# 
#  示例 4： 
# 
#  输出：s = "xxyyzz", t = "xxyyzz"
# 输出：0
#  
# 
#  示例 5： 
# 
#  输出：s = "friend", t = "family"
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 50000 
#  s.length == t.length 
#  s 和 t 只包含小写英文字母 
#  
#  Related Topics 字符串

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    题目要求制造字母异位词，所以字母的位置不需要考虑???
    只能看示例数据得出
    """

    def minSteps(self, s: str, t: str) -> int:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        diff = counter_t - counter_s
        return sum(diff.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="bab", t="aba"), 1],
    [dict(s="leetcode", t="practice"), 5],
    [dict(s="anagram", t="mangaar"), 0],
    [dict(s="xxyyzz", t="xxyyzz"), 0],
    [dict(s="friend", t="family"), 4],
])
def test_solutions(kw, expected):
    assert Solution().minSteps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
