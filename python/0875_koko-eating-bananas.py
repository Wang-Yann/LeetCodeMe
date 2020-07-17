#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:48:19
# @Last Modified : 2020-05-03 14:48:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
#
#  珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后
# 这一小时内不会再吃更多的香蕉。
#
#  珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
#
#  返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
#
#
#
#
#
#
#  示例 1：
#
#  输入: piles = [3,6,7,11], H = 8
# 输出: 4
#
#
#  示例 2：
#
#  输入: piles = [30,11,23,4,20], H = 5
# 输出: 30
#
#
#  示例 3：
#
#  输入: piles = [30,11,23,4,20], H = 6
# 输出: 23
#
#
#
#
#  提示：
#
#
#  1 <= piles.length <= 10^4
#  piles.length <= H <= 10^9
#  1 <= piles[i] <= 10^9
#
#  Related Topics 二分查找
#  👍 78 👎 0

"""

import math
from typing import List

import pytest


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """ Math.ceil(p / K) = ((p-1) // K) + 1"""
        def possible(K):
            # Can Koko eat all bananas in H hours with eating speed K?
            return sum([math.ceil(p/K) for p in piles]) <= H

        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) >> 1
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kwargs,expected", [
    (dict(piles=[3, 6, 7, 11], H=8), 4),
    (dict(piles=[30, 11, 23, 4, 20], H=5), 30),
    (dict(piles=[30, 11, 23, 4, 20], H=6), 23),
])
def test_solutions(kwargs, expected):
    assert Solution().minEatingSpeed(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
