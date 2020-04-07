#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-07 21:42:49
# @Last Modified : 2020-04-07 21:42:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        A=height
        result = 0
        stack = []

        for i in range(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height

                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])

        return result


if __name__ == '__main__':
    sol = Solution()
    sample=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(sample))



