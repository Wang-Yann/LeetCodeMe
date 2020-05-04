#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 13:36:41
# @Last Modified : 2020-05-04 13:36:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1,num2 = num1[::-1],num2[::-1]
        num1_len,num2_len=map(len,[num1,num2])
        res=[0]*(num1_len+num2_len)
        for i in range(num1_len):
            for j in range(num2_len):
                res[i+j] +=int(num1[i])*int(num2[j])
                res[i+j+1]+=res[i+j]//10
                res[i+j]%=10
        i = len(res)-1
        while i>0 and res[i]==0:
            i-=1
        return "".join(map(str,res[i::-1]))



@pytest.mark.parametrize("kwargs,expected", [
    (dict(num1 = "2", num2 = "3"), "6"),
    pytest.param(dict(num1 = "123", num2 = "456"), "56088"),
])
def test_solutions(kwargs, expected):
    assert Solution().multiply(**kwargs) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


