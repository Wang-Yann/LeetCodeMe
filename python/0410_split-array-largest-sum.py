#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 16:43:04
# @Last Modified : 2020-04-30 16:43:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        TODO
        https://leetcode-cn.com/problems/split-array-largest-sum/solution/410-by-ikaruga/
        """

        def canSplit(nums, m, split_sum):
            cnt, cur_sum = 1, 0
            for num in nums:
                cur_sum += num
                if cur_sum > split_sum:
                    cur_sum = num
                    cnt += 1
            return cnt <= m

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) >> 1
            if canSplit(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kw,expected", [
    (dict(nums=[7, 2, 5, 10, 8],
          m=2), 18)
])
def test_solutions(kw, expected):
    assert Solution().splitArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
