#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 13:42:09
# @Last Modified : 2020-04-29 13:42:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 实现 int sqrt(int x) 函数。
#
#  计算并返回 x 的平方根，其中 x 是非负整数。
#
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
#  示例 1:
#
#  输入: 4
# 输出: 2
#
#
#  示例 2:
#
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
#
#  Related Topics 数学 二分查找
#  👍 446 👎 0

"""

import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right


@pytest.mark.parametrize("args", [
    (4, 2),
    (8, 2),
    (11, 3),
    pytest.param((11, 7), marks=pytest.mark.xfail),
])
def test_solution(args):
    sol = Solution()
    *args, expected = args
    assert sol.mySqrt(*args) == pytest.approx(expected, abs=1e-3)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
