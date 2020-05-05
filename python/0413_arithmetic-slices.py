#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:01:17
# @Last Modified : 2020-05-05 15:01:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans, i = 0, 0
        length = len(A)
        while i < length - 2:
            start = i
            while i < length - 2 and A[i + 2] + A[i] == 2 * A[i + 1]:
                ans += i - start + 1
                i += 1
            i += 1
        return ans


class Solution1:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """DP
        dp[i] 用来存储在区间 (k,i)， 而不在区间 (k,j)中等差数列的个数，
        """
        length = len(A)
        dp = [0] * length
        # ans=0
        for i in range(2, length):
            if A[i - 2] + A[i] == 2 * A[i - 1]:
                dp[i] = dp[i - 1] + 1
                # ans+=dp[i]
        print(dp)
        return sum(dp)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4], 3),
    ([7, 7, 7, 7], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8], 21),
    ([1, 3, 5, 7, 9, 15, 20, 25, 28], 7)
])
def test_solutions(args, expected):
    assert Solution().numberOfArithmeticSlices(args) == expected
    assert Solution1().numberOfArithmeticSlices(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
