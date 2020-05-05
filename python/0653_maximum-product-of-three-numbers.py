#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:09:36
# @Last Modified : 2020-05-05 17:09:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        length = len(nums)
        if length < 3:
            return 0
        return max([
            nums[-1] * nums[-2] * nums[0],
            nums[-1] * nums[0] * nums[1],
            nums[0] * nums[1] * nums[2]
        ])


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 6),
    pytest.param([1, 2, 3, 4], 24),
])
def test_solutions(args, expected):
    assert Solution().maximumProduct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
