#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:44:59
# @Last Modified : 2020-05-05 16:44:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import re

import pytest


class Solution:

    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ints = list(map(int, re.findall("[+-]?\d+", expression)))
        # print(ints)
        A, B = 0, 1
        for i in range(0, len(ints), 2):
            a, b = ints[i], ints[i + 1]
            A = A * b + a * B
            B *= b
            g = gcd(A, B)
            A //= g
            B //= g
        return "%d/%d" % (A, B)


@pytest.mark.parametrize("args,expected", [
    ("-1/2+1/2", "0/1"),
    ("5/3+1/3", "2/1"),
    pytest.param("-1/2+1/2+1/3", "1/3"),
    pytest.param("1/3-1/2", "-1/6"),
])
def test_solutions(args, expected):
    assert Solution().fractionAddition(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
