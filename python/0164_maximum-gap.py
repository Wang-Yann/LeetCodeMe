#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 11:54:17
# @Last Modified : 2020-05-01 11:54:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        pre = nums[0]
        max_gap = float("-inf")
        for v  in nums:
            max_gap = max(max_gap,v-pre)
            pre =v
        return  max_gap


@pytest.mark.parametrize("args,expected", [
    ([3, 6, 9, 1], 3),
    pytest.param([10], 0),
])
def test_solutions(args, expected):
    assert Solution().maximumGap(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
