#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 22:16:15
# @Last Modified : 2020-04-11 22:16:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        (1,1)-->(m,n)
        F(m,n) = F(m-1,n)+F(m,n-1)
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for row in range(1, m+1):
            for col in range(1, n+1):

                if obstacleGrid[row-1][col-1]==1:
                    dp[row][col] =0
                elif row==1 and col==1:
                    continue
                else:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m][n]




if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ],
        [
            [0,0,0],
            [1,1,0],
            [0,0,0]
        ],
        [[1]]
    ]
    res = [sol.uniquePathsWithObstacles(x) for x in samples]
    print(res)
