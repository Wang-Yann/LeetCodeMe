#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 09:28:13
# @Last Modified : 2020-04-29 09:28:13
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# （这是一个 交互式问题 ）
#
#  给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index
# 值。
#
#  如果不存在这样的下标 index，就请返回 -1。
#
#
#
#  何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
#
#  首先，A.length >= 3
#
#  其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
#
#
#  A[0] < A[1] < ... A[i-1] < A[i]
#  A[i] > A[i+1] > ... > A[A.length - 1]
#
#
#
#
#  你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
#
#
#  MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
#  MountainArray.length() - 会返回该数组的长度
#
#
#
#
#  注意：
#
#  对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
#
#  为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请
# 注意这 不是一个正确答案。
#
#
#
#
#
#
#  示例 1：
#
#  输入：array = [1,2,3,4,5,3,1], target = 3
# 输出：2
# 解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
#
#  示例 2：
#
#  输入：array = [0,1,2,4,2,1], target = 3
# 输出：-1
# 解释：3 在数组中没有出现，返回 -1。
#
#
#
#
#  提示：
#
#
#  3 <= mountain_arr.length() <= 10000
#  0 <= target <= 10^9
#  0 <= mountain_arr.get(index) <= 10^9
#
#  Related Topics 二分查找
#  👍 85 👎 0


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
                                lambda x:mountain_arr.get(x) >= mountain_arr.get(x + 1))
        left = binarySearch(0, one_peak, lambda x:mountain_arr.get(x) >= target)
        if left <= one_peak and mountain_arr.get(left) == target:
            return left
        right = binarySearch(one_peak, mountain_arr.length() - 1,
                             lambda x:mountain_arr.get(x) <= target)
        if right <= mountain_arr.length() - 1 and mountain_arr.get(right) == target:
            return right
        return -1


def binarySearch(l, r, check_func):
    while l <= r:
        mid = l + ((r - l) >> 1)
        # print("l,r,mid", l, r, mid)
        if check_func(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l


def test_binary_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 4, 1]
    peak = binarySearch(0, len(array) - 1, lambda x:array[x] >= array[x + 1])
    assert peak == 7
    assert binarySearch(0, peak, lambda x:array[x] >= 4) == 3
    assert binarySearch(4, len(array) - 1, lambda x:array[x] <= 4) == 8


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
