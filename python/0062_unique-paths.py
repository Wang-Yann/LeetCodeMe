#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 22:16:15
# @Last Modified : 2020-04-11 22:16:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        (1,1)-->(m,n)
        F(m,n) = F(m-1,n)+F(m,n-1)
        """
        # if m==1 or n ==1: return 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[1][1] = 1
        for row in range(1, m+1):
            for col in range(1, n+1):
                if row==1 and col==1:
                    continue
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m][n]

    def uniquePathsS(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]

        return ways[n - 1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [3, 2],
        [7, 3],
        [99, 66],
        [1, 1],
        [1, 10],
        [10, 1]
    ]
    res = [sol.uniquePaths(x, y) for x, y in samples]
    print(res)
