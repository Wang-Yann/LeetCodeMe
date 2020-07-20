#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:27:11
# @Last Modified : 2020-05-10 18:27:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
#
#
#  示例 1:
#
#  输入: [10,2]
# 输出: "102"
#
#  示例 2:
#
#  输入: [3,30,34,5,9]
# 输出: "3033459"
#
#
#
#  提示:
#
#
#  0 < nums.length <= 100
#
#
#  说明:
#
#
#  输出结果可能非常大，所以你需要返回一个字符串而不是整数
#  拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
#
#  Related Topics 排序
#  👍 63 👎 0



import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Comparator(str):
    def __lt__(self, other):
        return self+other<other+self

class Solution:

    def minNumber(self, nums: List[int]) -> str:

        nums = [str(x) for x in nums]
        nums.sort(key = Comparator)
        return "".join(nums)


@pytest.mark.parametrize("args,expected", [
    ([10,2],  "102"),
    pytest.param([3,30,34,5,9], "3033459"),
])
def test_solutions(args, expected):
    assert Solution().minNumber(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


