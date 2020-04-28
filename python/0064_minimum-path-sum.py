#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 14:18:15
# @Last Modified : 2020-04-12 14:18:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        m,n = len(grid),len(grid[0])
        dp = [ [0 for _ in range(n+1) ] for _ in range(m+1)]
        for col in range(n+1):
            dp[0][col]=float("inf")
        for row in range(m+1):
            dp[row][0]=float("inf")
        for i in range(1,m+1):
            for j in  range(1,n+1):
                if i==1 and j ==1:
                    dp[i][j] = grid[0][0]
                    continue
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i-1][j-1]
        return dp[m][n]

    def minPathSumS(self, grid):
        sum = list(grid[0])
        for j in range(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            sum[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

        return sum[-1]


if __name__ == '__main__':
    sol = Solution()
    samples=[
        [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]
    ]
    res = [ sol.minPathSum(x) for x in samples]
    print(res)


