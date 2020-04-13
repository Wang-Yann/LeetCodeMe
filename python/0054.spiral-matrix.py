#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 17:56:21
# @Last Modified : 2020-04-11 17:56:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        res = []
        m,n = len(matrix),len(matrix[0])
        cnt = 0
        min_i,min_j=0,0
        max_i,max_j=m-1,n-1
        direction = 0
        while cnt< m*n:
            #--->
            if direction ==0:
                for idx in range(min_j,max_j+1):
                    res.append(matrix[min_i][idx])
                    cnt+=1
                min_i +=1
            #|
            #V
            elif direction==1:
                for idx in range(min_i,max_i+1):
                    res.append(matrix[idx][max_j])
                    cnt+=1
                max_j -=1
            #<--
            elif direction==2:
                for idx in range(max_j,min_j-1,-1):
                    res.append(matrix[max_i][idx])
                    cnt+=1
                max_i-=1
            #^
            #|
            elif direction==3:
                for idx in range(max_i,min_i-1,-1):
                    res.append(matrix[idx][min_j])
                    cnt+=1
                min_j +=1
            direction=(direction+1)%4
        return res



if __name__ == '__main__':
    sol = Solution()
    sample=[
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    sample1 =[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        # [13,14,15,16]
    ]
    sample2 =[[1]]
    sample3 =[[1,2],
              [3,4]]
    sample4 =[
        [1, 2, 3, 4 ,5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25],
    ]
    print(sol.spiralOrder(sample))
    print(sol.spiralOrder(sample1))
    print(sol.spiralOrder(sample2))
    print(sol.spiralOrder(sample3))
    print(sol.spiralOrder(sample4))