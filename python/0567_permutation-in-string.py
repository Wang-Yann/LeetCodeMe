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
        need = collections.Counter(s1)
        window = collections.Counter()
        left, right = 0, 0
        length = len(s2)
        valid = 0
        while right < length:
            char = s2[right]
            right += 1
            if need[char]:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1
            while right >= len(s1) + left:
                if valid == len(need):
                    return True
                char_d = s2[left]
                left += 1
                if need[char_d]:
                    if window[char_d] == need[char_d]:
                        valid -= 1
                    window[char_d] -= 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kwargs,expected", [
    (dict(s1="ab", s2="eidbaooo"), True),
    pytest.param(dict(s1="ab", s2="eidboaoo"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().checkInclusion(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
