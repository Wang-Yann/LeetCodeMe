#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 13:39:18
# @Last Modified : 2020-05-05 13:39:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Good
        """
        subsets ={-1:set()}
        for num in sorted(nums):
            subsets[num]=max([ subsets[k] for k in subsets if num%k==0 ],key=len ) | {num}
        # print(subsets)
        return list(max(subsets.values(),key=len))


@pytest.mark.parametrize("args,expected", [
    ([1,2,3], [[1,3],[1,2]]),
    pytest.param([1,2,4,8], [[1,2,4,8]]),
])
def test_solutions(args, expected):
    assert sorted(Solution().largestDivisibleSubset(args)) in expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


