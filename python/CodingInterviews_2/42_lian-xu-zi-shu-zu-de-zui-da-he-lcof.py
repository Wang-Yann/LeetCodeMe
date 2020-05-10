#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 17:59:35
# @Last Modified : 2020-05-10 17:59:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur,ans =float("-inf"),float("-inf")
        for v in nums:
            max_cur = max(v,max_cur+v)
            ans = max(ans,max_cur)
        return ans


@pytest.mark.parametrize("args,expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
])
def test_solutions(args, expected):
    assert Solution().maxSubArray(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


