#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 22:32:41
# @Last Modified : 2020-04-30 22:32:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math

import pytest


class Solution:

    def smallestGoodBase(self, n: str) -> str:
        """
        看不懂
        TODO
        """
        num = int(n)
        max_len = int(math.log(num, 2))
        for l in range(max_len, 1, -1):
            b = int(num ** (l ** (-1)))
            if (b ** (l + 1) - 1) // (b - 1) == num:
                return str(b)
        return str(num - 1)



@pytest.mark.parametrize("args,expected", [
    ("13", "3"),
    pytest.param("4681", "8"),
    pytest.param("1000000000000000000", "999999999999999999"),
])
def test_solutions(args, expected):
    assert Solution().smallestGoodBase(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
