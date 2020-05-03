#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:13:50
# @Last Modified : 2020-05-03 16:13:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(0,len(A)-2):
            if A[i+1]+A[i+2]>A[i]:
                return  A[i+1]+A[i+2]+A[i]
        return 0



@pytest.mark.parametrize("args,expected", [
    ([2, 1, 2], 5),
    ([1, 2, 1], 0),
    ([3, 2, 3, 4], 10),
    ([3, 6, 2, 3], 8),
    ([1, 2, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().largestPerimeter(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
