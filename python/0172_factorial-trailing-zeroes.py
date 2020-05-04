#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:21:59
# @Last Modified : 2020-05-04 20:21:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n = n // 5
        return res


@pytest.mark.parametrize("args,expected", [
    (3, 0),
    pytest.param(5, 1),
])
def test_solutions(args, expected):
    assert Solution().trailingZeroes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
