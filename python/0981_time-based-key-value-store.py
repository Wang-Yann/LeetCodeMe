#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:20:47
# @Last Modified : 2020-05-03 16:20:47
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import bisect
import collections

import pytest


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.lookup.get(key)
        if not A:
            return ""
        i = bisect.bisect_right(A, (timestamp + 1, 0))
        return A[i - 1][1] if i else ""


def test_solution():
    obj = TimeMap()
    ops_list = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    args_list = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
