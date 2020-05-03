#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:18:23
# @Last Modified : 2020-05-03 14:18:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) >> 1
            if A[mid] > A[mid + 1]:
                r = mid -1
            else:
                l = mid +1
        return l


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 0], 1),
    pytest.param([0, 2, 1, 0], 1),
])
def test_solutions(args, expected):
    assert Solution().peakIndexInMountainArray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
