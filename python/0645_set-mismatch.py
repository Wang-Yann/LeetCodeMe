#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:30:54
# @Last Modified : 2020-05-05 17:30:54
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr=[0]*(n+1)
        dup,missing=-1,1
        for v in nums:
            arr[v]+=1
        for i in range(1,n+1):
            if arr[i]==0:
                missing=i
            elif arr[i]==2:
                dup=i
        return [dup,missing]

class Solution1(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x_xor_y = 0
        for i in range(len(nums)):
            x_xor_y ^= nums[i] ^ (i+1)
        bit =  x_xor_y & ~(x_xor_y-1)
        result = [0] * 2
        for i, num in enumerate(nums):
            result[bool(num & bit)] ^= num
            result[bool((i+1) & bit)] ^= i+1
        if result[0] not in nums:
            result[0], result[1] = result[1], result[0]
        return result

@pytest.mark.parametrize("args,expected", [
    ([1,2,2,4], [2,3]),
    ([1,1], [1,2]),
])
def test_solutions(args, expected):
    assert Solution().findErrorNums(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


