#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:53:06
# @Last Modified : 2020-04-30 15:53:06
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。
 

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。


"""
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


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


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
    assert Solution1().kthSmallest(matrix, k) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
