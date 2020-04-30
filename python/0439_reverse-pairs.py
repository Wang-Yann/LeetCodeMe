#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 22:56:37
# @Last Modified : 2020-04-30 22:56:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, start, mid, end):
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start + len(tmp)] = tmp

        def countAndMergeSort(nums, start, end):
            if end - start <= 0:
                return 0
            mid = (start + end) >> 1
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
            merge(nums, start, mid, end)
            return count

        return countAndMergeSort(nums, 0, len(nums) - 1)


@pytest.mark.parametrize("args,expected", [
    ([1, 3, 2, 3, 1], 2),
    pytest.param([2, 4, 3, 5, 1], 3),
])
def test_solutions(args, expected):
    assert Solution().reversePairs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
