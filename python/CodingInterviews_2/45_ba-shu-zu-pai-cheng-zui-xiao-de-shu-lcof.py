#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:27:11
# @Last Modified : 2020-05-10 18:27:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Comparator(str):
    def __lt__(self, other):
        return self+other<other+self

class Solution:

    def minNumber(self, nums: List[int]) -> str:

        nums = [str(x) for x in nums]
        nums.sort(key = Comparator)
        return "".join(nums)


@pytest.mark.parametrize("args,expected", [
    ([10,2],  "102"),
    pytest.param([3,30,34,5,9], "3033459"),
])
def test_solutions(args, expected):
    assert Solution().minNumber(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


