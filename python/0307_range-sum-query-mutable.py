#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 nums，求出数组从索引 i 到 j (i ≤ j) 范围内元素的总和，包含 i, j 两点。 
# 
#  update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。 
# 
#  示例: 
# 
#  Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#  
# 
#  说明: 
# 
#  
#  数组仅可以在 update 函数下进行修改。 
#  你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。 
#  
#  Related Topics 树状数组 线段树

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:
    """
    线段树
    """

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.tree_arr = self.size * [0] + nums
        for i in range(self.size - 1, 0, -1):
            # i's sons are 2i, 2i + 1
            self.tree_arr[i] = self.tree_arr[i << 1] + self.tree_arr[(i << 1) + 1]

    def update(self, i: int, val: int) -> None:
        i += self.size
        self.tree_arr[i] = val
        while i > 1:
            # if i is odd, left is i - 1, if i is even, right is i + 1
            self.tree_arr[i >> 1] = self.tree_arr[i] + self.tree_arr[i ^ 1]
            i >>= 1

    def sumRange(self, i: int, j: int) -> int:
        l, r = i + self.size, j + self.size
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree_arr[l]
                l += 1
            l >>= 1
            if not r & 1:
                res += self.tree_arr[r]
                r -= 1
            r >>= 1
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)
class NumArray1:
    """
    树状数组
    """

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i, self.arr[i])

    def update(self, i: int, val: int) -> None:
        self._add(i, val - self.arr[i])
        self.arr[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self._sum(j) - self._sum(i - 1)

    @staticmethod
    def _lowbit(x):
        return x & (-x)

    def _add(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += self._lowbit(idx)

    def _sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= self._lowbit(idx)
        return res


@pytest.mark.parametrize("Datastruct", [
    (NumArray1),
    (NumArray),
])
def test_solutions(Datastruct):
    nums = [1, 3, 5]
    sol = Datastruct(nums)
    assert sol.sumRange(0, 2) == 9
    sol.update(1, 2)
    assert sol.sumRange(0, 2) == 8


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
