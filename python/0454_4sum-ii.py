#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:40:50
# @Last Modified : 2020-04-30 17:40:50
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from typing import List

import pytest


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A_B_sum=collections.Counter(a+b for a in A for b in B)
        res = sum(A_B_sum[-c-d] for c in C for d in D)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(
        A=[1, 2],
        B=[-2, -1],
        C=[-1, 2],
        D=[0, 2]
    ), 2]
])
def test_solutions(kw, expected):
    assert Solution().fourSumCount(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
