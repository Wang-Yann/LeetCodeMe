#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 22:24:30
# @Last Modified : 2020-05-01 22:24:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i
# ] 成正比。
#
#
#
#
#  例如，给定一个值 [1，9] 的输入列表，当我们从中选择一个数字时，很有可能 10 次中有 9 次应该选择数字 9 作为答案。
#
#
#
#  示例 1：
#
#  输入：
# ["Solution","pickIndex"]
# [[[1]],[]]
# 输出：[null,0]
#
#
#  示例 2：
#
#  输入：
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# 输出：[null,0,1,1,1,0]
#
#
#
#  输入语法说明：
#
#  输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有一个参数，即数组 w。pickIndex 没有参数。输入参数是一个列表，即使参数
# 为空，也会输入一个 [] 空列表。
#
#
#
#  提示：
#
#
#  1 <= w.length <= 10000
#  1 <= w[i] <= 10^5
#  pickIndex 将被调用不超过 10000 次
#
#  Related Topics 二分查找 Random
#  👍 39 👎 0

"""

import bisect
from random import randint
from typing import List

import pytest


class Solution:

    def __init__(self, w: List[int]):
        self.__prefix_sum = list(w)
        for i in range(1, len(w)):
            self.__prefix_sum[i] += self.__prefix_sum[i - 1]

    def pickIndex(self) -> int:
        target = randint(0, self.__prefix_sum[-1] - 1)
        return bisect.bisect_right(self.__prefix_sum, target)


def test_solution():
    obj = Solution([1, 3])
    # ops_list = ["Solution","pick","pick","pick"]
    # args_list =[[[[1,1,5,5]]],[],[],[]]
    ops_list = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    args_list = [[[1, 3]], [], [], [], [], []]
    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
