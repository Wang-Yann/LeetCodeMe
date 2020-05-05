#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 19:09:37
# @Last Modified : 2020-05-05 19:09:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List

import pytest


class Solution:

    def numRabbits(self, answers: List[int]) -> int:
        """
        HARD
        """
        counter = collections.Counter(answers)
        ret = 0
        for k, v in counter.items():
            ret+=v+((k+1-v)%(k+1))
        return ret


@pytest.mark.parametrize("args,expected", [
    ([1, 1, 2], 5),
    ([], 0),
    pytest.param([10, 10, 10], 11),
])
def test_solutions(args, expected):
    assert Solution().numRabbits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
