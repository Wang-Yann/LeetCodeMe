#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-14 22:04:05
# @Last Modified : 2020-04-14 22:04:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-"1"."0"

from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp(i,j) 表示的是由 1 组成的最大正方形的边长；
        从 (0,0)(0,0) 开始，对原始矩阵中的每一个 1，我们将当前元素的值更新为
        \text{dp}(i,\ j) = \min \big( \text{dp}(i-1,\ j),\ \text{dp}(i-1,\ j-1),\ \text{dp}(i,\ j-1) \big) + 1
        dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1

        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_side = 0
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["1", "1", "1", "0", "0"],
            ["1", "0", "1", "0", "0"]
        ]
    ]
    res = [sol.maximalSquare(x) for x in samples]
    print(res)
