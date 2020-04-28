#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:34:46
# @Last Modified : 2020-04-22 23:34:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m,n =  len(matrix),len(matrix[0])
        i,j=0,n-1
        while i<=m-1 and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False



if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(sol.findNumberIn2DArray(samples, 5))
    print(sol.findNumberIn2DArray(samples, 20))
    print(sol.findNumberIn2DArray([[20]], 20))
