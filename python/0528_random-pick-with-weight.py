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

    def __init__(self, w: List[int]):
        self.__prefix_sum = list(w)
        for i in range(1, len(w)):
            self.__prefix_sum[i] += self.__prefix_sum[i - 1]

    def pickIndex(self) -> int:
        target = randint(0, self.__prefix_sum[-1] - 1)
        return bisect.bisect_right(self.__prefix_sum, target)


if __name__ == '__main__':
    obj = Solution([1, 3])
    # ops_list = ["Solution","pick","pick","pick"]
    # args_list =[[[[1,1,5,5]]],[],[],[]]
    ops_list = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    args_list = [[[1, 3]], [], [], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
