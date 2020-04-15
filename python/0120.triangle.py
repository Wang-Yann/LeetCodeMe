#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 20:46:14
# @Last Modified : 2020-04-15 20:46:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from functools import reduce
from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        if not m:
            return 0
        dp = [[float("inf")] * (m + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, i + 1):
                if i == 1 and j == 1:
                    dp[i][j] = triangle[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i - 1][j - 1]
        return reduce(min, dp[-1])

    def minimumTotalS(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        cur = triangle[0] + [float("inf")]
        for i in range(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in range(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]
        return reduce(min, cur)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]

    ]
    res = [sol.minimumTotalS(x) for x in samples]
    print(res)
