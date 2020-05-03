#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 19:13:27
# @Last Modified : 2020-05-03 19:13:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def myAtoi(self, str: str) -> int:
        ans =0
        length=len(str)
        i=0
        while i<length and  str[i].isspace():
            i+=1
        if i==length:
            return ans
        sign=1
        if  str[i] =="+":
            i+=1
        elif str[i]=="-":
            sign=-1
            i+=1
        INT_MIN = -2**31
        INT_MAX = -(INT_MIN+1)
        while i<length and str[i].isdigit():
            cur_bit=ord(str[i])-ord('0')
            if ans>(INT_MAX-cur_bit)//10:
                return INT_MAX if sign>0 else INT_MIN
            ans=ans*10+cur_bit
            i+=1

        return  ans*sign

@pytest.mark.parametrize("args,expected", [
    ("",0),
    ("42",42),
    ("    -42",-42),
    ("4193 with words",4193),
    ("words and 987",0),
    ("-91283472332",-2147483648),
    ("91283472332",2147483647),
    ("-2147483648",-2147483648),
])
def test_solutions(args, expected):
    assert Solution().myAtoi(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


