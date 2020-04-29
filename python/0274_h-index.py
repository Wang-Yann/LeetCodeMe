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
    def hIndex0(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        for i, v in enumerate(citations):
            if length - i <= v:
                return length-i 
        return 0

    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        i=0
        while i<length and  citations[length-1-i]>i:
            i+=1
        return i


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 3, 5, 6], 3),
    ([3, 0, 6, 1, 5], 3),
    ([0], 0),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.hIndex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
