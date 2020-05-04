#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:47:10
# @Last Modified : 2020-05-04 20:47:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
from typing import List
import collections, bisect, heapq
import functools, itertools


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:return False
        cnt =0
        while n:
            if n&0b1:
                cnt+=1
            n>>=1
        return cnt==1

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0

@pytest.mark.parametrize("args,expected", [
    (1, True),
    (16, True),
    (218, False),
    (-16, False),
])
def test_solutions(args, expected):
    assert Solution().isPowerOfTwo(args) == expected
    assert Solution1().isPowerOfTwo(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


