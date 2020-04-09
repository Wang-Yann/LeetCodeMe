#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-08 11:22:18
# @Last Modified : 2020-04-08 11:22:18
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    bit_array = []

    def movingCount(self, m: int, n: int, k: int) -> int:
        area_matrix = [[0 for _ in range(n)] for _ in range(m)]
        self.bit_array = [self.getNumBitSum(x) for x in range(max(m, n))]
        res = self.dfs(area_matrix, m - 1, n - 1, 0, 0, k)
        return res

    def getNumBitSum(self, num: int) -> int:
        v = 0
        while num > 0:
            v += num % 10
            num //= 10
        return v

    def dfs(self, area_array: List[List[int]], rows: int, cols: int, i: int, j: int, k: int):
        if i < 0 or i > rows or j < 0 or j > cols or area_array[i][j] or self.bit_array[i] + self.bit_array[j] > k:
            return 0
        area_array[i][j] = 1
        return 1 + self.dfs(area_array, rows, cols, i, j - 1, k) \
               + self.dfs(area_array, rows, cols, i, j + 1, k) \
               + self.dfs(area_array, rows, cols, i - 1, j, k) \
               + self.dfs(area_array, rows, cols, i + 1, j, k)


if __name__ == '__main__':
    sol = Solution()
    m = 2
    n = 3
    k = 1
    print(sol.movingCount(m, n, k))
    print(sol.movingCount(11, 11, 5))
    print(sol.movingCount(3, 1, 0))
