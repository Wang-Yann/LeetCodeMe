#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:50:53
# @Last Modified : 2020-05-05 18:50:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def isIdealPermutation(self, A: List[int]) -> bool:
        """
        https://leetcode-cn.com/problems/global-and-local-inversions/solution/quan-ju-dao-zhi-yu-ju-bu-dao-zhi-by-leetcode/
        理想 数组的充分必要条件为 Math.abs(A[i] - i) <= 1

        """
        return all(abs(v - i) <= 1 for i, v in enumerate(A))


class Solution1:

    def isIdealPermutation(self, A: List[int]) -> bool:
        """
       ************ 一个局部倒置也是一个全局倒置，因此只需要检查有没有非局部倒置 ***********************
        暴力法中需要检查是否存在满足 j >= i+2 的 A[i] > A[j]，这和检查 A[i] > min(A[i+2:]) 是等价的。如果提前计算出 min(A[0:]), min(A[1:]), min(A[2:]), ... 这些区间的最小值，就可以立即完成检查操作


        """
        length = len(A)
        floor = length
        for i in range(length - 1, 1, -1):
            floor = min(floor, A[i])
            if A[i - 2] > floor:
                return False
        return True


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 2], True),
    pytest.param([1, 2, 0], False),
])
def test_solutions(args, expected):
    assert Solution().isIdealPermutation(args) == expected
    assert Solution1().isIdealPermutation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
