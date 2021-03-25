#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。 
# 
#  换句话说，第一个字符串的排列之一是第二个字符串的子串。 
# 
#  示例1: 
# 
#  
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
# 
#  
# 
#  示例2: 
# 
#  
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#  
# 
#  
# 
#  注意： 
# 
#  
#  输入的字符串只包含小写字母 
#  两个字符串的长度都在 [1, 10,000] 之间 
#  
#  Related Topics 双指针 Sliding Window

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        window = collections.Counter()
        left, right = 0, 0
        N = len(s2)
        satisfied = 0
        while right < N:
            char = s2[right]
            right += 1
            if target[char]:
                window[char] += 1
                if window[char] == target[char]:
                    satisfied += 1
            while right - left > len(s1):
                char_l = s2[left]
                left += 1
                if target[char_l]:
                    if window[char_l] == target[char_l]:
                        satisfied -= 1
                    window[char_l] -= 1
            if satisfied == len(target):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def checkInclusion(self, s1, s2):

        target = collections.Counter(s1)
        N = len(s1)
        window = collections.Counter()
        for r, char in enumerate(s2):
            window[char] += 1
            if r >= N:
                l_char = s2[r - N]
                window[l_char] -= 1
                if window[l_char] == 0:
                    window.pop(l_char)
            if window == target:
                return True
        return False


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s1="ab", s2="eidbaooo"), True),
    pytest.param(dict(s1="ab", s2="eidboaoo"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().checkInclusion(**kwargs) == expected
    assert Solution1().checkInclusion(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
