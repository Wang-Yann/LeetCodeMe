#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:38:03
# @Last Modified : 2020-05-05 18:38:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def reachNumber(self, target: int) -> int:
        """
        https://leetcode-cn.com/problems/reach-a-number/solution/dao-da-zhong-dian-shu-zi-by-leetcode/
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        if target%2==0:
            return k
        else:
            return k+1+k%2


@pytest.mark.parametrize("args,expected", [
    (3,2),
    pytest.param(2, 3),
])
def test_solutions(args, expected):
    assert Solution().reachNumber(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


