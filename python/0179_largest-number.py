#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 20:12:02
# @Last Modified : 2020-05-01 20:12:02
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import functools
from typing import List

import pytest


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        def comp_func(x, y):
            if (x + y) > (y + x):
                return -1
            elif (x + y) > (y + x):
                return 1
            else:
                return 0

        nums_str = [str(x) for x in nums]
        nums_str.sort(key=functools.cmp_to_key(comp_func))
        res = "".join(nums_str)
        return res.lstrip("0") or "0"


class LargerNumKey(str):

    def __lt__(x, y):
        return x + y > y + x


class Solution1:

    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


@pytest.mark.parametrize("args,expected", [
    ([10, 2], "210"),
    pytest.param([3, 30, 34, 5, 9], "9534330"),
])
def test_solutions(args, expected):
    assert Solution().largestNumber(args) == expected
    assert Solution1().largestNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
