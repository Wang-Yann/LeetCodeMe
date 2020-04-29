#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 16:52:51
# @Last Modified : 2020-04-29 16:52:51
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        length = len(citations)
        l, r = 0, length - 1
        #查找第一个value >=length-i 时　的l
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] > length - mid:
                r -= 1
            elif citations[mid] < length - mid:
                l += 1
            else:
                return length-mid
        return length - l


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 3, 5, 6], 3),
    ([], 0),
    ([0], 0),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.hIndex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
