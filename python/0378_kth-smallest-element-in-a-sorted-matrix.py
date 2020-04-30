#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:53:06
# @Last Modified : 2020-04-30 15:53:06
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import heapq
from typing import List

import pytest


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """最小堆"""
        rows, cols = len(matrix), len(matrix[0])
        min_heap = []
        ans = 0

        # def push(i, j):
        #     if rows > cols:
        #         if i < cols and j < rows:
        #             heapq.heappush(min_heap, (matrix[j][i], i, j))
        #     else:
        #         if i < rows and j < cols:
        #             heapq.heappush(min_heap, (matrix[i][j], i, j))
        def push(i, j):
            if i < rows and j < cols:
                heapq.heappush(min_heap, (matrix[i][j], i, j))

        push(0, 0)
        while min_heap and k > 0:
            ans, i, j = heapq.heappop(min_heap)
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
            k -= 1
        return ans


@pytest.mark.parametrize("matrix", [
    [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
])
@pytest.mark.parametrize("k,expected", [
    [8, 13],
    [2, 5],
])
def test_solutions(matrix, k, expected):
    assert Solution().kthSmallest(matrix, k) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
