#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:05:11
# @Last Modified : 2020-05-05 17:05:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for op in ops:
            m=min(m,op[0])
            n=min(n,op[1])
        return m*n


@pytest.mark.parametrize("kwargs,expected", [
    (dict(m=3, n=3, ops=[[2, 2], [3, 3]]), 4)
])
def test_solutions(kwargs, expected):
    assert Solution().maxCount(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
