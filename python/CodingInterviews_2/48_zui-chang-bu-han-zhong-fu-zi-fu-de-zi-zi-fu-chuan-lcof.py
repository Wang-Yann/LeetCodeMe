#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 19:20:16
# @Last Modified : 2020-05-10 19:20:16
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
#
#
#  示例 1:
#
#  输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
#  提示：
#
#
#  s.length <= 40000
#
#
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-rep
# eating-characters/
#  Related Topics 哈希表 双指针 Sliding Window
#  👍 63 👎 0


import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口
        """
        length =len(s)
        hash_set = set()
        res,left,right = 0,0,0
        while left<=length-1 and right <=length-1:
            if s[right] not in hash_set:
                hash_set.add(s[right])
                right+=1
                res=max(res,right-left)
            else:
                hash_set.discard(s[left])
                left+=1
        return res



@pytest.mark.parametrize("args,expected", [
    ("abcabcbb", 3),
    ("", 0),
    ("pwwkew", 3),
    pytest.param("bbbbb", 1),
])
def test_solutions(args, expected):
    assert Solution().lengthOfLongestSubstring(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


