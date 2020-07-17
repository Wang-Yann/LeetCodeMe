#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 15:34:42
# @Last Modified : 2020-04-12 15:34:42
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  示例 1:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
#  示例 2:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#  Related Topics 数组 二分查找
#  👍 209 👎 0

"""

from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        high_row, high_col = len(matrix)-1, len(matrix[0])-1
        low_row, low_col = 0, 0
        searched_row = -1
        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            if matrix[mid_row][-1] < target:
                low_row = mid_row + 1
            elif matrix[mid_row][0] > target:
                high_row = mid_row - 1
            # elif matrix[mid_row][0] == target or matrix[mid_row][-1]==target:
            #     return True
            else:
                searched_row = mid_row
                break
        if searched_row == -1:
            return False
        print("Searched_Row",searched_row)
        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2
            if matrix[searched_row][mid_col] < target:
                low_col = mid_col + 1
            elif matrix[searched_row][mid_col] > target:
                high_col = mid_col - 1
            else:
                return True
        return False
    def searchMatrixS(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        #二分查找
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False



if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 3),
        ([
             [1, 3, 5, 7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]
         ], 13),
        ([[1]],0),
        ([[1]],1),
        ([[1,3]],1),
        ([[1],[3]],3),
        ([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3)
    ]
    res = [sol.searchMatrix(m, target) for m, target in samples]
    print(res)
