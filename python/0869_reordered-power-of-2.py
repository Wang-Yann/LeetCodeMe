#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:43:25
# @Last Modified : 2020-05-05 22:43:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """ 既然 N 只能是 2 的幂，我们只需要检查 NN 跟这些幂是不是拥有一样数字构成"""
        count =collections.Counter(str(N))
        return any(count == collections.Counter(str(1<<b)) for b in range(31))


@pytest.mark.parametrize("args,expected", [
    (1, True),
    (10, False),
    (16, True),
    (24, False),
    (46, True),
    (281, True),
])
def test_solutions(args, expected):
    assert Solution().reorderedPowerOf2(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


