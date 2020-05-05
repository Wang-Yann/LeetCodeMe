#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:16:14
# @Last Modified : 2020-05-05 14:16:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maxRotateFunction(self, A: List[int]) -> int:
        """
        错位相减
        F(k+1) = F(k) + S - n * Bk[n-1]
        """
        sum_val = sum(A)
        fi = 0
        for i, v in enumerate(A):
            fi += i * v
        result = fi
        for i in range( len(A)-1,0,-1):
            fi += sum_val - len(A) * A[i]
            result = max(result, fi)
        return result


@pytest.mark.parametrize("args,expected", [
    ([4, 3, 2, 6], 26),
])
def test_solutions(args, expected):
    assert Solution().maxRotateFunction(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
