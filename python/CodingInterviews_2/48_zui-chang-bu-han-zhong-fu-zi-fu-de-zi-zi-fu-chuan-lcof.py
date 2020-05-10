#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 19:20:16
# @Last Modified : 2020-05-10 19:20:16
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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


