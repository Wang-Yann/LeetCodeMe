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
    def addStrings(self, num1: str, num2: str) -> str:
        num1,num2 = num1[::-1],num2[::-1]
        num1_len,num2_len=map(len,[num1,num2])
        max_len=max(num1_len,num2_len)
        ans=""
        carry =0
        for i in range(max_len):
            v1 = int(num1[i]) if i<num1_len else 0
            v2 = int(num2[i]) if i<num2_len else 0
            cur=v1+v2+carry
            carry=cur//10
            ans=str(cur%10)+ans
        if carry:
            ans=str(carry)+ans
        return ans


class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i,j,carry =  len(num1)-1,len(num2)-1,0
        while i>=0 or j>=0 or carry:
            if i>=0:
                carry+=ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                carry+=ord(num2[j])-ord('0')
                j-=1
            res.append(str(carry%10))
            carry//=10
        return "".join(res[::-1])



@pytest.mark.parametrize("kwargs,expected", [
    (dict(num1 = "2", num2 = "3"), "5"),
    (dict(num1 = "6", num2 = "5"), "11"),
    pytest.param(dict(num1 = "128", num2 = "456"), "584"),
])
def test_solutions(kwargs, expected):
    assert Solution().addStrings(**kwargs) == expected
    assert Solution1().addStrings(**kwargs) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


