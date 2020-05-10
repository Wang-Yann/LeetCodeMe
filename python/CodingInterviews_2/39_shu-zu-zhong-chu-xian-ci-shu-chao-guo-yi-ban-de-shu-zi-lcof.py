#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 17:40:27
# @Last Modified : 2020-05-10 17:40:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import collections
from typing import List

import pytest


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        most = collections.Counter(nums).most_common(1)
        return most[0][0]


class Solution1:
    """摩尔投票法： 核心理念为 “正负抵消” """

    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            if x == num:
                votes += 1
            else:
                votes -= 1

        return x


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 2, 2, 2, 5, 4, 2], 2),
])
def test_solutions(args, expected):
    assert Solution().majorityElement(args) == expected
    assert Solution1().majorityElement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
