#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 20:12:02
# @Last Modified : 2020-05-01 20:12:02
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
#  示例 1:
#
#  输入: [10,2]
# 输出: 210
#
#  示例 2:
#
#  输入: [3,30,34,5,9]
# 输出: 9534330
#
#  说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#  Related Topics 排序
#  👍 327 👎 0

"""
import functools
from typing import List

import pytest


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        def comp_func(x, y):
            if (x + y) > (y + x):
                return -1
            elif (x + y) > (y + x):
                return 1
            else:
                return 0

        nums_str = [str(x) for x in nums]
        nums_str.sort(key=functools.cmp_to_key(comp_func))
        res = "".join(nums_str)
        return res.lstrip("0") or "0"


class LargerNumKey(str):

    def __lt__(x, y):
        return x + y > y + x


class Solution1:

    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


@pytest.mark.parametrize("args,expected", [
    ([10, 2], "210"),
    pytest.param([3, 30, 34, 5, 9], "9534330"),
])
def test_solutions(args, expected):
    assert Solution().largestNumber(args) == expected
    assert Solution1().largestNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
