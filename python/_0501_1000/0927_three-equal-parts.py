#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:30:23
# @Last Modified : 2020-05-03 15:30:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。
#
#  如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
#
#
#  A[0], A[1], ..., A[i] 组成第一部分；
#  A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
#  A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
#  这三个部分所表示的二进制值相等。
#
#
#  如果无法做到，就返回 [-1, -1]。
#
#  注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,
# 1,1] 和 [1,1] 表示相同的值。
#
#
#
#  示例 1：
#
#  输入：[1,0,1,0,1]
# 输出：[0,3]
#
#
#  示例 2：
#
#  输出：[1,1,0,1,1]
# 输出：[-1,-1]
#
#
#
#  提示：
#
#
#  3 <= A.length <= 30000
#  A[i] == 0 或 A[i] == 1
#
#
#
#  Related Topics 贪心算法 数学 二分查找
#  👍 29 👎 0

"""
from typing import List

import pytest


class Solution:

    def threeEqualParts(self, A: List[int]) -> List[int]:
        """HARD"""
        total = sum(A)
        length = len(A)
        if total % 3 != 0:
            return [-1, -1]
        if total == 0:
            return [0, length - 1]
        count = total // 3
        nums = [0] * 3
        c = 0
        for i in range(length):
            if A[i] == 1:
                if c % count == 0:
                    nums[c // count] = i
                c += 1
        # print(nums)
        while nums[2] != length:
            # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
            # where [i1, j1] is a block of 1s, etc.
            if not A[nums[0]] == A[nums[1]] == A[nums[2]]:
                return [-1, -1]
            nums[0] += 1
            nums[1] += 1
            nums[2] += 1
        # print(nums)
        return [nums[0] - 1, nums[1]]


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 1, 0, 1], [0, 3]),
    # pytest.param([1, 1, 0, 1, 1], [-1, -1]),
])
def test_solutions(args, expected):
    assert Solution().threeEqualParts(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
