#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 19:35:35
# @Last Modified : 2020-05-10 19:35:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = collections.Counter(s)
        for char in s:
            if counter[char]==1:
                return char
        return " "



class Solution1:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for char in s:
            dic[char]=dic.get(char,0)+1
        for k,v in dic.items():
            if v==1:
                return k
        return " "

@pytest.mark.parametrize("args,expected", [
    ("abaccdeff", "b"),
    pytest.param(""," "),
])
def test_solutions(args, expected):
    assert Solution().firstUniqChar(args) == expected
    assert Solution1().firstUniqChar(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


