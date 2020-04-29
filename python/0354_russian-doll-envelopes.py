#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 22:15:23
# @Last Modified : 2020-04-29 22:15:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """在对信封按 w 进行排序以后，我们可以找到 h 上最长递增子序列的长度。"""
        LIS = []

        def insert(target):
            l, r = 0, len(LIS) - 1
            while l <= r:
                mid = (l + r) >> 1
                if LIS[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            if len(LIS) == l:
                LIS.append(target)
            else:
                LIS[l] = target
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        for envelope in envelopes:
            insert(envelope[1])
        print(LIS )
        return len(LIS)


@pytest.mark.parametrize("args,expected", [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    pytest.param([[1,2]], 1),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.maxEnvelopes(args) == expected

if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
