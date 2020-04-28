#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math
import os
import sys
import traceback
from typing import List


class Solution:

    def getCn(self, n, i):
        if i == 0 or n==i:
            return 1
        res = 1
        for v in range(n,n-i,-1):
            res *= v
        for vv in range(1, i+1):
            res //= vv
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        n = rowIndex
        res = [self.getCn(n, i) for i in range(rowIndex+1)]
        return res


if __name__ == '__main__':
    sol = Solution()
    sample = []
    print(sol.getRow(3))
    print(sol.getRow(2))
    print(sol.getRow(5))
    print(sol.getRow(5))
