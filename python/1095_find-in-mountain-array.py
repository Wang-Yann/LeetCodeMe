#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 09:28:13
# @Last Modified : 2020-04-29 09:28:13
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import pytest


class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution:
    """仅具参考意义"""

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        先使用二分法找到数组的峰值。
        在峰值左边使用二分法寻找目标值。
        如果峰值左边没有目标值，那么使用二分法在峰值右边寻找目标值
        """

        def binarySearch(l, r, check_func):
            """
            TODO
            重点：优先级：[+-]>[>><<]>[&]>[<= >=]
            注意理解下
            例如　找峰值[1, 2, 3, 4, 5,6,7, 8,4, 1]

            """
            while l <= r:
                mid = l + ((r - l) >> 1)
                # 注意等号尽量往左边缩减,l==r了在由l往右增
                if check_func(mid):
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        one_peak = binarySearch(0, mountain_arr.length() - 1,
                                lambda x: mountain_arr.get(x) >= mountain_arr.get(x + 1))
        left = binarySearch(0, one_peak, lambda x: mountain_arr.get(x) >= target)
        if left <= one_peak and mountain_arr.get(left) == target:
            return left
        right = binarySearch(one_peak, mountain_arr.length() - 1,
                             lambda x: mountain_arr.get(x) <= target)
        if right <= mountain_arr.length() - 1 and mountain_arr.get(right) == target:
            return right
        return -1


def binarySearch(l, r, check_func):
    while l <= r:
        mid = l + ((r - l) >> 1)
        print("l,r,mid", l, r, mid)
        if check_func(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l


def test_binary_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 4, 1]
    peak = binarySearch(0, len(array) - 1, lambda x: array[x] >= array[x + 1])
    assert peak == 7
    assert binarySearch(0, peak, lambda x: array[x] >= 4) == 3
    assert binarySearch(4, len(array) - 1, lambda x: array[x] <= 4) == 8


@pytest.mark.parametrize("args", [
    (3, MountainArray([1, 2, 3, 4, 5, 3, 1]), 2),
    (3, MountainArray([0, 1, 2, 4, 2, 1]), -1),
    (4, MountainArray([1, 2, 3, 4, 5, 6, 7, 8, 4, 1]), 3),
    (8, MountainArray([1, 2, 3, 4, 5, 6, 7, 8, 4, 1]), 7),

])
def test_solution(args):
    sol = Solution()
    *args, expected = args
    assert sol.findInMountainArray(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q",
                 # "--pdbcls=IPython.terminal.debugger:TerminalPdb",
                 # "--show-capture=all",
                 "--color=yes", __file__])
