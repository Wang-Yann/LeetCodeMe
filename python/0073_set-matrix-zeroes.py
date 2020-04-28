#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 14:54:42
# @Last Modified : 2020-04-12 14:54:42
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:return
        m,n = len(matrix),len(matrix[0])
        clean_rows = set( )
        clean_cols = set( )
        i=0
        while i<=m-1:
            for j in range(n):
                if  matrix[i][j]==0:
                    clean_rows.add(i)
                    clean_cols.add(j)
            i+=1
        for i in clean_rows:
            for col in range(n):
                matrix[i][col]=0
        for j in clean_cols:
            for row in range(m):
                matrix[row][j]=0




if __name__ == '__main__':
    sol = Solution()
    samples=[
        # [
        #     [1,1,1],
        #     [1,0,1],
        #     [1,1,1]
        # ],
        # [
        #     [0,1,2,0],
        #     [3,4,5,2],
        #     [1,3,1,5]
        # ],
        # [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
        # [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]],
        [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

    ]
    res = [ sol.setZeroes(x) for x in samples]
    print(samples)

