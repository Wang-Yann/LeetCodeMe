#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 23:15:40
# @Last Modified : 2020-05-01 23:15:40
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import bisect
from typing import List

import pytest


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """TODO"""
        length = len(arr)
        idx = bisect.bisect_left(arr, x)
        left, right = idx - 1, idx
        while k:
            if right >= length or (left >= 0 and abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left + 1:right]


class SolutionMe:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v:abs(v - x))
        return sorted(arr[0:k])


@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[1, 2, 3, 4, 5], k=4, x=3), [1, 2, 3, 4]),
    pytest.param(dict(arr=[1, 2, 3, 4, 5], k=4, x=-1), [1, 2, 3, 4]),
])
def test_solutions(kwargs, expected):
    assert (Solution().findClosestElements(**kwargs)) == expected
    assert (SolutionMe().findClosestElements(**kwargs)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
