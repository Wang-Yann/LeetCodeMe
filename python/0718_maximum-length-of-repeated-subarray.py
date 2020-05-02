#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:21:34
# @Last Modified : 2020-05-02 14:21:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        设 dp[i][j] 为 A[i:] 和 B[j:] 的最长公共前缀，那么答案就为所有 dp[i][j] 中的最大值 max(dp[i][j])。
        如果 A[i] == B[j]，那么状态转移方程为 dp[i][j] = dp[i + 1][j + 1] + 1，否则状态转移方程为 dp[i][j] = 0。

        """
        len_A, len_B = len(A), len(B)
        dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]
        for i in range(len_A - 1, -1, -1):
            for j in range(len_B - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        print(dp)
        return max(max(row) for row in dp)


@pytest.mark.parametrize("A,B,expected", [
    ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
    ([0,0,0,0,1], [1,0,0,0,0], 4),
])
def test_solutions(A,B, expected):
    assert Solution().findLength(A,B) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
