#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:30:23
# @Last Modified : 2020-05-03 15:30:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def threeEqualParts(self, A: List[int]) -> List[int]:
        """HARD"""
        total = sum(A)
        length = len(A)
        if total % 3 != 0:
            return [-1, -1]
        if total == 0:
            return [0, length - 1]
        count = total // 3
        nums = [0] * 3
        c = 0
        for i in range(length):
            if A[i] == 1:
                if c % count == 0:
                    nums[c // count] = i
                c += 1
        # print(nums)
        while nums[2] != length:
            # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
            # where [i1, j1] is a block of 1s, etc.
            if not A[nums[0]] == A[nums[1]] == A[nums[2]]:
                return [-1, -1]
            nums[0] += 1
            nums[1] += 1
            nums[2] += 1
        # print(nums)
        return [nums[0] - 1, nums[1]]


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 1, 0, 1], [0, 3]),
    # pytest.param([1, 1, 0, 1, 1], [-1, -1]),
])
def test_solutions(args, expected):
    assert Solution().threeEqualParts(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
