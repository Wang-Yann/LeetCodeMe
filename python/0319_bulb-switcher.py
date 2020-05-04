#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 22:57:22
# @Last Modified : 2020-05-04 22:57:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math

import pytest


class Solution:

    def bulbSwitch(self, n: int) -> int:
        """完全平方数的因数的个数是奇数个"""
        return int(math.sqrt(n))


@pytest.mark.parametrize("args,expected", [
    (3, 1),
])
def test_solutions(args, expected):
    assert Solution().bulbSwitch(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
