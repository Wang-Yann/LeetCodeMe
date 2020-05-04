#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 16:24:26
# @Last Modified : 2020-05-04 16:24:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import string

import pytest


class Solution:

    def titleToNumber(self, s: str) -> str:
        base=26
        char_map = dict(zip(string.ascii_uppercase ,range(1,base+1)))
        res = 0
        for char in  s:
            res = res*base+ char_map[char]
        return res


@pytest.mark.parametrize("expected,s", [
    (1, "A"),
    (701, "ZY"),
    pytest.param(28, "AB"),
])
def test_solutions( expected,s):
    assert Solution().titleToNumber(s) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
