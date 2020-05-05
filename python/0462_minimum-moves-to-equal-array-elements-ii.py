#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:35:18
# @Last Modified : 2020-05-05 15:35:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)



@pytest.mark.parametrize("args,expected", [
    ([1,2,3], 2),
    ([1,0,0,8,6], 14),
])
def test_solutions(args, expected):
    assert Solution().minMoves2(args) == expected







if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


