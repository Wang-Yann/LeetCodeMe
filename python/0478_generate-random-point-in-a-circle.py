#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:43:38
# @Last Modified : 2020-05-05 15:43:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import math
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.__radius = radius
        self.__x = x_center
        self.__y = y_center

    def randPoint(self) -> List[float]:
        r = self.__radius * math.sqrt(random.uniform(0, 1))
        theta = (2 * math.pi) * random.uniform(0, 1)
        return [self.__x + r * math.cos(theta), self.__y + r * math.sin(theta)]


if __name__ == '__main__':
    obj = Solution(1, 0, 0)
    ops_list = ["Solution", "randPoint", "randPoint", "randPoint"]
    args_list = [[1, 0, 0], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
