#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 16:10:18
# @Last Modified : 2020-07-21 16:10:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t ，并返回该子串的长度。 
# 
#  示例 1: 
# 
#  输入: "eceba"
# 输出: 3
# 解释: t 是 "ece"，长度为3。
#  
# 
#  示例 2: 
# 
#  输入: "ccaabbb"
# 输出: 5
# 解释: t 是 "aabbb"，长度为5。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 49 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """AC """
        window = collections.Counter()
        l = 0
        ans = 0
        for r, char in enumerate(s):
            window[char] += 1
            while len(window) > 2:
                l_char = s[l]
                window[l_char] -= 1
                if window[l_char] == 0:
                    window.pop(l_char)
                l += 1
            ans = max(ans, sum(window.values()))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("eceba", 3),
    ("", 0),
    ("ccaabbb", 5),
])
def test_solutions(args, expected):
    assert Solution().lengthOfLongestSubstringTwoDistinct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
