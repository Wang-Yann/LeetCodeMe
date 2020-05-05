#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 13:14:12
# @Last Modified : 2020-05-05 13:14:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def isSelfCrossing(self, x: List[int]) -> bool:
        """https://leetcode-cn.com/problems/self-crossing/solution/335lu-jing-jiao-cha-by-zhangll/"""
        length = len(x)
        if length >= 5 and x[3] == x[1] and x[4] + x[0] >= x[2]:
            # Crossing in a loop:
            #     2
            # 3 ┌────┐
            #   └─══>┘1
            #   4  0  (overlapped)
            return True
        for i in range(3, length):
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                # Case 1:
                #    i-2
                # i-1┌─┐
                #    └─┼─>i
                #     i-3
                return True
            elif i >= 5 \
                    and x[i - 4] <= x[i - 2] <= x[i] + x[i - 4] \
                    and x[i - 1] <= x[i - 3] <= x[i - 5] + x[i - 1]:
                # Case 2:
                #    i-4
                #    ┌──┐
                #    │i<┼─┐
                # i-3│ i-5│i-1
                #    └────┘
                #      i-2
                return True
        return False

class Solution1:
    def isSelfCrossing(self, x) -> bool:
        if len(x) <  4:return False
        if len(x) == 4:return   x[3] >= x[1] and x[2] <= x[0]
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i > 3 and x[i-1] == x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True
            if i > 4 and x[i-3]-x[i-5] <= x[i-1] <= x[i-3] and x[i-2]-x[i-4] <= x[i] <= x[i-2] and x[i-2] > x[i-4]:
                return True
        return False



@pytest.mark.parametrize("args,expected", [
    ([2, 1, 1, 2], True),
    ([1, 1, 1, 1], True),
    pytest.param([1, 2, 3, 4], False),
])
def test_solutions(args, expected):
    assert Solution().isSelfCrossing(args) == expected
    assert Solution1().isSelfCrossing(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
