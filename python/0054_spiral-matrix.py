#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 17:56:21
# @Last Modified : 2020-04-11 17:56:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        min_i, min_j = 0, 0
        max_i, max_j = m - 1, n - 1
        direction = 0
        while cnt < m * n:
            # --->
            if direction == 0:
                for idx in range(min_j, max_j + 1):
                    res.append(matrix[min_i][idx])
                    cnt += 1
                min_i += 1
            # |
            # V
            elif direction == 1:
                for idx in range(min_i, max_i + 1):
                    res.append(matrix[idx][max_j])
                    cnt += 1
                max_j -= 1
            # <--
            elif direction == 2:
                for idx in range(max_j, min_j - 1, -1):
                    res.append(matrix[max_i][idx])
                    cnt += 1
                max_i -= 1
            # ^
            # |
            elif direction == 3:
                for idx in range(max_i, min_i - 1, -1):
                    res.append(matrix[idx][min_j])
                    cnt += 1
                min_j += 1
            direction = (direction + 1) % 4
        return res


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      ], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1]], [1]),
    ([[1, 2],
      [3, 4]], [1, 2, 4, 3]),
    ([[1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25],
      ], [1, 2, 3, 4, 5, 10, 15, 20, 25, 24,
          23, 22, 21, 16, 11, 6, 7, 8, 9, 14,
          19, 18, 17, 12, 13]),
])
def test_solutions(args, expected):
    assert Solution().spiralOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
