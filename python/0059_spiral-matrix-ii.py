#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 17:56:21
# @Last Modified : 2020-04-11 17:56:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
#  示例:
#
#  输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#  Related Topics 数组
#  👍 207 👎 0

"""
from typing import List

import pytest


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        min_i, min_j = 0, 0
        max_i, max_j = n - 1, n - 1
        direction = 0
        cnt = 1
        while cnt <= n * n:
            # --->
            if direction == 0:
                for idx in range(min_j, max_j + 1):
                    matrix[min_i][idx] = cnt
                    cnt += 1
                min_i += 1
            # |
            # V
            elif direction == 1:
                for idx in range(min_i, max_i + 1):
                    matrix[idx][max_j] = cnt
                    cnt += 1
                max_j -= 1
            # <--
            elif direction == 2:
                for idx in range(max_j, min_j - 1, -1):
                    matrix[max_i][idx] = cnt
                    cnt += 1
                max_i -= 1
            # ^
            # |
            elif direction == 3:
                for idx in range(max_i, min_i - 1, -1):
                    matrix[idx][min_j] = cnt
                    cnt += 1
                min_j += 1
            direction = (direction + 1) % 4

        return matrix


@pytest.mark.parametrize("args,expected", [
    (1, [[1]]),
    (3, [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
     ),
    (4, [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]
     ),
])
def test_solutions(args, expected):
    assert Solution().generateMatrix(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
