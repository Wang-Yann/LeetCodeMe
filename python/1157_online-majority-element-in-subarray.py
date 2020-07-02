#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 实现一个 MajorityChecker 的类，它应该具有下述几个 API： 
# 
#  
#  MajorityChecker(int[] arr) 会用给定的数组 arr 来构造一个 MajorityChecker 的实例。 
#  int query(int left, int right, int threshold) 有这么几个参数：
#  
#  0 <= left <= right < arr.length 表示数组 arr 的子数组的长度。 
#  2 * threshold > right - left + 1，也就是说阈值 threshold 始终比子序列长度的一半还要大。 
#  
#  
#  
# 
#  每次查询 query(...) 会返回在 arr[left], arr[left+1], ..., arr[right] 中至少出现阈值次数 thresh
# old 的元素，如果不存在这样的元素，就返回 -1。 
# 
#  
# 
#  示例： 
# 
#  MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // 返回 1
# majorityChecker.query(0,3,3); // 返回 -1
# majorityChecker.query(2,3,2); // 返回 2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 20000 
#  1 <= arr[i] <= 20000 
#  对于每次查询，0 <= left <= right < len(arr) 
#  对于每次查询，2 * threshold > right - left + 1 
#  查询次数最多为 10000 
#  
#  Related Topics 线段树 数组 二分查找

"""
import bisect
import collections
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class MajorityChecker:

    def __init__(self, arr: List[int]):
        a2i = collections.defaultdict(list)
        for i, v in enumerate(arr):
            a2i[v].append(i)
        self.arr = arr
        self.a2i = a2i
        self.nums = sorted(self.a2i.keys(), key=lambda n:len(self.a2i[n]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        for v in self.nums:
            if len(self.a2i[v]) < threshold:
                return -1
            l = bisect.bisect_left(self.a2i[v], left)
            r = bisect.bisect_right(self.a2i[v], right)
            if r - l >= threshold:
                return v
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# leetcode submit region end(Prohibit modification and deletion)

class SegmentTreeRecu(object):  # 0-based index

    def __init__(self, nums, count):
        """
        ##复制过来的  TODO

        """
        N = len(nums)
        self.__original_length = N
        self.__tree_length = 2 ** (N.bit_length() + (N & (N - 1) != 0)) - 1
        self.__tree = [-1 for _ in range(self.__tree_length)]
        self.__count = count
        self.__constructTree(nums, 0, self.__original_length - 1, 0)

    def query(self, i, j):
        return self.__queryRange(i, j, 0, self.__original_length - 1, 0)

    def __constructTree(self, nums, left, right, idx):
        if left > right:
            return
        if left == right:
            self.__tree[idx] = nums[left]
            return
        mid = left + (right - left) // 2
        self.__constructTree(nums, left, mid, idx * 2 + 1)
        self.__constructTree(nums, mid + 1, right, idx * 2 + 2)
        if self.__tree[idx * 2 + 1] != -1 and \
                self.__count(self.__tree[idx * 2 + 1], left, right) * 2 > right - left + 1:
            self.__tree[idx] = self.__tree[idx * 2 + 1]
        elif self.__tree[idx * 2 + 2] != -1 and \
                self.__count(self.__tree[idx * 2 + 2], left, right) * 2 > right - left + 1:
            self.__tree[idx] = self.__tree[idx * 2 + 2]

    def __queryRange(self, range_left, range_right, left, right, idx):
        if left > right:
            return -1, -1
        if right < range_left or left > range_right:
            return -1, -1
        if range_left <= left and right <= range_right:
            if self.__tree[idx] != -1:
                c = self.__count(self.__tree[idx], range_left, range_right)
                if c * 2 > range_right - range_left + 1:
                    return self.__tree[idx], c
        else:
            mid = left + (right - left) // 2
            result = self.__queryRange(range_left, range_right, left, mid, idx * 2 + 1)
            if result[0] != -1:
                return result
            result = self.__queryRange(range_left, range_right, mid + 1, right, idx * 2 + 2)
            if result[0] != -1:
                return result
        return -1, -1


class MajorityChecker1(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """

        def count(inv_idx, m, left, right):
            return bisect.bisect_right(inv_idx[m], right) - \
                   bisect.bisect_left(inv_idx[m], left)

        self.__arr = arr
        self.__inv_idx = collections.defaultdict(list)
        for i, x in enumerate(self.__arr):
            self.__inv_idx[x].append(i)
        self.__segment_tree = SegmentTreeRecu(arr, functools.partial(count, self.__inv_idx))

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        result = self.__segment_tree.query(left, right)
        if result[1] >= threshold:
            return result[0]
        return -1


def test_solution():
    majorityChecker = MajorityChecker([1, 1, 2, 2, 1, 1])
    assert majorityChecker.query(0, 5, 4) == 1  # 返回 1
    assert majorityChecker.query(0, 3, 3) == -1  # 返回 -1
    assert majorityChecker.query(2, 3, 2) == 2  # 返回 2


def test_solution1():
    majorityChecker = MajorityChecker1([1, 1, 2, 2, 1, 1])
    assert majorityChecker.query(0, 5, 4) == 1  # 返回 1
    assert majorityChecker.query(0, 3, 3) == -1  # 返回 -1
    assert majorityChecker.query(2, 3, 2) == 2  # 返回 2


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
