#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 10:52:47
# @Last Modified : 2020-04-30 10:52:47
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:
    """归并排序+前缀和"""

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countAndMergeSort(sums, start, end):
            #左闭右开
            # The size of range [start, end) less than 2 is always with count 0.
            if end - start <= 1:
                return 0
            mid = (start + end) >> 1
            count = countAndMergeSort(sums, start, mid) + \
                    countAndMergeSort(sums, mid, end)
            Upper, Lower, rPos = mid, mid, mid
            tmp = []
            l =start
            for i in range(l, mid):
                # Count the number of range sums that lie in [lower, upper].
                while Lower < end and sums[Lower] - sums[i] < lower:
                    Lower += 1
                while Upper < end and sums[Upper] - sums[i] <= upper:
                    Upper += 1
                count += Upper - Lower
                # Merge the two sorted arrays into tmp.
                while rPos < end and sums[rPos] < sums[i]:
                    tmp.append(sums[rPos])
                    rPos += 1
                tmp.append(sums[i])
            # Copy tmp back to sums.
            sums[start:start + len(tmp)] = tmp
            print("tmp,sums",tmp,sums )
            return count

        sums = [0] * (len(nums) + 1)
        for idx in range(len(nums)):
            sums[idx + 1] = sums[idx] + nums[idx]
        return countAndMergeSort(sums, 0, len(sums))


@pytest.mark.parametrize("args,expected", [
    (([-2, 5, -1], -2, 2), 3)
])
def test_solutions(args, expected):
    assert Solution().countRangeSum(*args) == expected


if __name__ == '__main__':
    # pytest -s            # disable all capturing
    # pytest --capture=sys # replace sys.stdout/stderr with in-mem files
    # pytest --capture=fd  # also point filedescriptors 1 and 2 to temp file
    pytest.main(["-q", "--color=yes","--capture=no", __file__])
