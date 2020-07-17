#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:08:57
# @Last Modified : 2020-05-05 14:08:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
#  示例 1:
#
#  输入: a = 2, b = [3]
# 输出: 8
#
#
#  示例 2:
#
#  输入: a = 2, b = [1,0]
# 输出: 1024
#  Related Topics 数学
#  👍 73 👎 0

"""

from typing import List

import pytest


class Solution:

    def superPow(self, a: int, b: List[int]) -> int:
        BASE = 1337

        def myPow(a, k):
            if k == 0:
                return 1
            a %= BASE
            if k % 2 == 1:
                return a * myPow(a, k - 1) % BASE
            else:
                sub = myPow(a, k // 2)
                return (sub * sub) % BASE

        res = 1
        for digit in b:
            res = myPow(res, 10) * myPow(a, digit) % BASE
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(a=2, b=[3]), 8),
    pytest.param(dict(a=2, b=[1, 0]), 1024),
])
def test_solutions(kwargs, expected):
    assert Solution().superPow(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
