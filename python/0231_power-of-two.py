#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:47:10
# @Last Modified : 2020-05-04 20:47:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
#  示例 1:
#
#  输入: 1
# 输出: true
# 解释: 20 = 1
#
#  示例 2:
#
#  输入: 16
# 输出: true
# 解释: 24 = 16
#
#  示例 3:
#
#  输入: 218
# 输出: false
#  Related Topics 位运算 数学
#  👍 218 👎 0


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


