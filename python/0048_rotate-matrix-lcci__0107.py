#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 16:01:34
# @Last Modified : 2020-04-07 16:01:34
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个 n × n 的二维矩阵表示一个图像。
#
#  将图像顺时针旋转 90 度。
#
#  说明：
#
#  你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
#  示例 1:
#
#  给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
#
#  示例 2:
#
#  给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#
#  Related Topics 数组
#  👍 493 👎 0

"""
   Do not return anything, modify matrix in-place instead.
   给定 matrix =
       [
         [1,2,3],
         [4,5,6],
         [7,8,9]
       ],
       原地旋转输入矩阵，使其变为:
       [
         [7,4,1],
         [8,5,2],
         [9,6,3]
       ]

"""
from pprint import pprint
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix: return
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    sol.rotate(matrix)
    sol.rotate(matrix2)
    pprint(matrix)
    pprint(matrix2)

    # [
    #     [15,13, 2, 5],
    #     [14, 3, 4, 1],
    #     [12, 6, 8, 9],
    #     [16, 7,10,11]
    # ]
