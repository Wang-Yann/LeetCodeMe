#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:19:14
# @Last Modified : 2020-05-05 17:19:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import re

import pytest


class Solution:

    def solveEquation(self, equation: str) -> str:
        a, b, side = 0, 0, 1
        for eq, sign, num, is_x in re.findall("(=)|([-+]?)(\d*)(x?)", equation):
            print("rows",[eq, sign, num, is_x])
            if eq:
                side = -1
            elif is_x:
                a += side * int(sign + "1") * int(num or 1)
            elif num:
                b -= side * int(sign + num)
        if a:
            return "x=%d" % (b // a)
        else:
            return 'No solution' if b else "Infinite solutions"


@pytest.mark.parametrize("args,expected", [
    ("x+5-3+x=6+x-2", "x=2"),
    ("x=x", "Infinite solutions"),
    ("2x=x", "x=0"),
    ("2x+3x-6x=x+2", "x=-1"),
    ("x=x+2", "No solution"),
])
def test_solutions(args, expected):
    assert Solution().solveEquation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
