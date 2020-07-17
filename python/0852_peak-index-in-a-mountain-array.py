#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:18:23
# @Last Modified : 2020-05-03 14:18:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 我们把符合下列属性的数组 A 称作山脉：
#
#
#  A.length >= 3
#  存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[
# A.length - 1]
#
#
#  给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.leng
# th - 1] 的 i 的值。
#
#
#
#  示例 1：
#
#  输入：[0,1,0]
# 输出：1
#
#
#  示例 2：
#
#  输入：[0,2,1,0]
# 输出：1
#
#
#
#  提示：
#
#
#  3 <= A.length <= 10000
#  0 <= A[i] <= 10^6
#  A 是如上定义的山脉
#
#
#
#  Related Topics 二分查找
#  👍 95 👎 0

"""

from typing import List

import pytest


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) >> 1
            if A[mid] > A[mid + 1]:
                r = mid -1
            else:
                l = mid +1
        return l


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 0], 1),
    pytest.param([0, 2, 1, 0], 1),
])
def test_solutions(args, expected):
    assert Solution().peakIndexInMountainArray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
