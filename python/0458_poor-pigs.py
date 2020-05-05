#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:29:12
# @Last Modified : 2020-05-05 15:29:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import math

import pytest


class Solution:

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """ https://leetcode-cn.com/problems/poor-pigs/solution/ke-lian-de-xiao-zhu-by-leetcode/"""
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))


@pytest.mark.parametrize("args,expected", [
    ((1000, 15, 60), 5),
])
def test_solutions(args, expected):
    assert Solution().poorPigs(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
