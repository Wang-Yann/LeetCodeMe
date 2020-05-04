#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 16:24:26
# @Last Modified : 2020-05-04 16:24:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import pytest


class Solution:

    def convertToTitle(self, n: int) -> str:
        base = 26
        # char_map = dict(zip(range(1,base+1),string.ascii_uppercase ))
        res = ""
        while n > 0:
            # 重点
            n -= 1
            res = chr(ord('A') + (n % base)) + res
            n //= base
        return res


@pytest.mark.parametrize("args,expected", [
    (1, "A"),
    (701, "ZY"),
    pytest.param(28, "AB"),
])
def test_solutions(args, expected):
    assert Solution().convertToTitle(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
