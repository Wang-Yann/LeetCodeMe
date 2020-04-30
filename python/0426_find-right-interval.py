#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:07:06
# @Last Modified : 2020-04-30 17:07:06
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import bisect
from typing import List

import pytest


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted((x[0], idx) for idx, x in enumerate(intervals))
        res = []
        for l, r in intervals:
            idx = bisect.bisect_left(sorted_intervals, (r,))
            res.append(sorted_intervals[idx][1] if idx < len(sorted_intervals) else -1)
        # print(sorted_intervals )
        return res


@pytest.mark.parametrize("args,expected", [
    ([[1, 2]], [-1]),
    ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
    ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
])
def test_solutions(args, expected):
    assert Solution().findRightInterval(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
