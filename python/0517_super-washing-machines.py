#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:05:59
# @Last Modified : 2020-05-05 16:05:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions
from typing import List
import collections, bisect, heapq
import functools, itertools
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """ 贪心
        https://leetcode-cn.com/problems/super-washing-machines/solution/chao-ji-xi-yi-ji-by-leetcode/
        HARD
        """
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n
        for i in range(n):
            # Change the number of dresses in the machines to
            # the number of dresses to be removed from this machine
            # (could be negative)
            machines[i] -= dress_per_machine

        # curr_sum is a number of dresses to move at this point,
        # max_sum is a max number of dresses to move at this point or before,
        # m is number of dresses to move out from the current machine.
        curr_sum = max_sum = res = 0
        for m in machines:
            curr_sum += m
            max_sum = max(max_sum, abs(curr_sum))
            res = max(res, max_sum, m)
        return res



@pytest.mark.parametrize("args,expected", [
    ([1,0,5], 3),
    ([0,3,0], 2),
    ([0,2,0], -1),
])
def test_solutions(args, expected):
    assert Solution().findMinMoves(args) == expected







if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


