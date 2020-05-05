#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:16:11
# @Last Modified : 2020-05-05 16:16:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt = 0
        lookup = {0:-1}
        # 我们使用 HashMap 来保存到第 ii 个元素为止的累积和
        for i,num in enumerate(nums):
            cnt+=num
            if k:
                cnt%=k
            if cnt in lookup:
                if i-lookup[cnt]>=2:
                    return True
            else:
                lookup[cnt]=i
        return False

@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[23,2,4,6,7], k = 6), True),
    pytest.param(dict(nums=[23,2,6,4,7], k = 6), True),
])
def test_solutions(kwargs, expected):
    assert Solution().checkSubarraySum(**kwargs) == expected







if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


