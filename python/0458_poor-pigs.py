#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:29:12
# @Last Modified : 2020-05-05 15:29:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 有 1000 只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在 15 分钟内死去。
#
#  问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？
#
#  回答这个问题，并为下列的进阶问题编写一个通用算法。
#
#
#
#  进阶:
#
#  假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出 “有毒” 水桶？这 n 只水桶里有且仅有一只有毒的桶。
#
#
#
#  提示：
#
#
#  可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
#  小猪喝完水后，必须有 m 分钟的冷却时间。在这段时间里，只允许观察，而不允许继续饮水。
#  任何给定的桶都可以无限次采样（无限数量的猪）。
#
#  Related Topics 数学
#  👍 118 👎 0

"""

import math

import pytest


class Solution:

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        https://leetcode-cn.com/problems/poor-pigs/solution/ke-lian-de-xiao-zhu-by-leetcode/
        """
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))


@pytest.mark.parametrize("args,expected", [
    ((1000, 15, 60), 5),
])
def test_solutions(args, expected):
    assert Solution().poorPigs(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
