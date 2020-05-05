#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:40:58
# @Last Modified : 2020-05-05 17:40:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        left, right = 0, 0
        max_idx = len(digits) - 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                left, right = i, max_idx
        print(left,right)
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))


@pytest.mark.parametrize("args,expected", [
    (2736, 7236),
    pytest.param(9973, 9973),
])
def test_solutions(args, expected):
    assert Solution().maximumSwap(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
