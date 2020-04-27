#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 11:37:53
# @Last Modified : 2020-04-27 11:37:53
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections


class FreqStack:
    """
    Good
    """

    def __init__(self):
        self.__freq = collections.Counter()
        self.__group = collections.defaultdict(list)
        self.__max_freq = 0

    def push(self, x: int) -> None:
        self.__freq[x] += 1
        if self.__freq[x] > self.__max_freq:
            self.__max_freq = self.__freq[x]
        self.__group[self.__freq[x]].append(x)

    def pop(self) -> int:
        x = self.__group[self.__max_freq].pop()
        if not self.__group[self.__max_freq]:
            self.__group.pop(self.__max_freq)
            self.__max_freq -= 1
        self.__freq[x] -= 1
        if not self.__freq[x]:
            self.__freq.pop(x)
        return x


if __name__ == '__main__':
    obj = FreqStack()
    ops_list = ["FreqStack", "push", "push", "push", "push",
                "push", "push", "pop", "pop", "pop", "pop"]
    args_list = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
        # print(method, args, obj)
