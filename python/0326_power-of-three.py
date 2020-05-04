#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:00:22
# @Last Modified : 2020-05-04 23:00:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math

import pytest


class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        """
        Key Point: is_integer
        """
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()


@pytest.mark.parametrize("args,expected", [
    (27, True),
    (0, False),
    (9, True),
    (45, False),
])
def test_solutions(args, expected):
    assert Solution().isPowerOfThree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
