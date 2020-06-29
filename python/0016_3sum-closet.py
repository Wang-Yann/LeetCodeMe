#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:59:18
# @Last Modified : 2020-04-06 14:59:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        res = float("inf")
        delta = float("inf")
        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    vv = nums[i] + nums[j] + nums[k]
                    if abs(vv - target) < abs(delta):
                        delta = vv - target
                        res = vv
                        if delta == 0:
                            return res

        return res


class Solution1:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        i = 0
        delta = float("inf")
        res = float("inf")
        while i < length - 2:
            j, k = i + 1, length - 1
            while j < k:
                v_sum = nums[i] + nums[j] + nums[k]
                delta_now = v_sum - target

                if delta_now == 0:
                    return v_sum
                elif delta_now < 0:
                    j += 1
                else:
                    k = k - 1
                if abs(delta_now) < delta:
                    delta = abs(delta_now)
                    res = v_sum
            i += 1
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-1, 2, 1, -4], target=1), 2],
    [dict(nums=[0, 1, 2], target=3), 3],
])
def test_solutions(kw, expected):
    assert Solution().threeSumClosest(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])