#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:13:50
# @Last Modified : 2020-05-03 16:13:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
#
#  如果不能形成任何面积不为零的三角形，返回 0。
#
#
#
#
#
#
#  示例 1：
#
#  输入：[2,1,2]
# 输出：5
#
#
#  示例 2：
#
#  输入：[1,2,1]
# 输出：0
#
#
#  示例 3：
#
#  输入：[3,2,3,4]
# 输出：10
#
#
#  示例 4：
#
#  输入：[3,6,2,3]
# 输出：8
#
#
#
#
#  提示：
#
#
#  3 <= A.length <= 10000
#  1 <= A[i] <= 10^6
#
#  Related Topics 排序 数学
#  👍 70 👎 0

"""


from typing import List

import pytest


class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(0,len(A)-2):
            if A[i+1]+A[i+2]>A[i]:
                return  A[i+1]+A[i+2]+A[i]
        return 0



@pytest.mark.parametrize("args,expected", [
    ([2, 1, 2], 5),
    ([1, 2, 1], 0),
    ([3, 2, 3, 4], 10),
    ([3, 6, 2, 3], 8),
    ([1, 2, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().largestPerimeter(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
