#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:return []
        res = [[1]]
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            prev = res[i - 1]
            for i in range(0, i - 1):
                temp.append(prev[i] + prev[i + 1])
            temp.append(1)
            res.append(temp)
        return res


if __name__ == '__main__':
    sol = Solution()
    sample = []
    print(sol.generate(3))
    print(sol.generate(2))
    print(sol.generate(7))
