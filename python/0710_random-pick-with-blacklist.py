#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:06:36
# @Last Modified : 2020-05-02 14:06:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import random
from typing import List


class Solution0:

    def __init__(self, N: int, blacklist: List[int]):
        self.__n = N - len(blacklist)
        blacklist.sort()
        self.__blacklist = blacklist

    def pick(self) -> int:
        index = random.randint(0, self.__n - 1)
        l, r = 0, len(self.__blacklist) - 1
        while l <= r:
            mid = (l + r) >> 1
            if index + mid < self.__blacklist[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return index + l


class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.__n = N - len(blacklist)
        self.__lookup = {}
        white = iter(set(range(self.__n, N)) - set(blacklist))
        for black in blacklist:
            if black < self.__n:
                self.__lookup[black] = next(white)

    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.__n - 1)
        return self.__lookup[index] if index in self.__lookup else index


if __name__ == '__main__':
    obj = Solution(4, [2])
    ops_list = ["Solution", "pick", "pick", "pick"]
    args_list = [[4, [2]], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
