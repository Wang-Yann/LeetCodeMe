#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 22:24:30
# @Last Modified : 2020-05-01 22:24:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import bisect
from random import randint

from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        """第 i 个矩形 rects [i] = [x1，y1，x2，y2]，其中 [x1，y1] 是左下角的整数坐标，[x2，y2] 是右上角的整数坐标"""
        self.__rects = rects
        self.__prefix_sum = list(map(lambda x:(x[2] - x[0] + 1) * (x[3] - x[1] + 1), rects))
        # 按序累加每个矩形的面积（即权重)
        for i in range(1, len(self.__prefix_sum)):
            self.__prefix_sum[i] += self.__prefix_sum[i - 1]

    def pick(self) -> List[int]:
        target = randint(0, self.__prefix_sum[-1] - 1)
        left = bisect.bisect_right(self.__prefix_sum, target)
        rect = self.__rects[left]
        width, height = rect[2] - rect[0] + 1, rect[3] - rect[1] + 1
        base = self.__prefix_sum[left] - width * height
        return [rect[0] + (target - base) % width, rect[1] + (target - base) // width]


if __name__ == '__main__':
    obj = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    # ops_list = ["Solution","pick","pick","pick"]
    # args_list =[[[[1,1,5,5]]],[],[],[]]
    ops_list = ["Solution", "pick", "pick", "pick", "pick", "pick"]
    args_list = [[[[-2, -2, -1, -1], [1, 0, 3, 0]]], [], [], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
