#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:36:16
# @Last Modified : 2020-05-05 22:36:16
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def binaryGap(self, N: int) -> int:
        ans = 0
        i=0
        #32位 int
        pre=32
        while N:
            if N&0b1==1:
                ans = max(ans,i-pre)
                pre=i
            i+=1
            N>>=1
        return ans





@pytest.mark.parametrize("args,expected", [
    (22, 2),
    (5, 2),
    (6, 1),
    (8, 0),
])
def test_solutions(args, expected):
    assert Solution().binaryGap(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


