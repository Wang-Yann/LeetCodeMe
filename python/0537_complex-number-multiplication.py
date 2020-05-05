#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:35:01
# @Last Modified : 2020-05-05 16:35:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def complexNumberMultiply(self, a: str, b: str) -> str:
        ra, ia = map(int, a[:-1].split("+"))
        rb, ib = map(int, b[:-1].split("+"))
        return "%d+%di" % (ra * rb - ia * ib, ra * ib + ia * rb)


@pytest.mark.parametrize("a,b,expected", [
    ("1+1i", "1+1i", "0+2i"),
    pytest.param("1+-1i", "1+-1i", "0+-2i"),
])
def test_solutions(a, b, expected):
    assert Solution().complexNumberMultiply(a, b) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
