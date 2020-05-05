#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 20:45:40
# @Last Modified : 2020-05-05 20:45:40
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import functools
import operator
from typing import List

import pytest


class Solution:

    def xorGame(self, nums: List[int]) -> bool:
        """
        小红必胜当且仅当 nums 数组的异或值为 0，或者 nums 数组的长度为偶数
        """
        return functools.reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0


@pytest.mark.parametrize("args,expected", [
    ([1, 1, 2], False),
])
def test_solutions(args, expected):
    assert Solution().xorGame(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
