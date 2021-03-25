#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 23:15:40
# @Last Modified : 2020-05-01 23:15:40
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一
# 样，优先选择数值较小的那个数。
#
#  示例 1:
#
#
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
#
#
#
#
#  示例 2:
#
#
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
#
#
#
#
#  说明:
#
#
#  k 的值为正数，且总是小于给定排序数组的长度。
#  数组不为空，且长度不超过 104
#  数组里的每个元素与 x 的绝对值不超过 104
#
#
#
#
#  更新(2017/9/19):
# 这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
#  Related Topics 二分查找
#  👍 111 👎 0

"""
import bisect
from typing import List

import pytest


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """TODO"""
        length = len(arr)
        idx = bisect.bisect_left(arr, x)
        left, right = idx - 1, idx
        while k:
            if right >= length or (left >= 0 and abs(arr[left] - x) <= abs(arr[right] - x)):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left + 1:right]


class SolutionMe:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v:abs(v - x))
        return sorted(arr[0:k])


@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[1, 2, 3, 4, 5], k=4, x=3), [1, 2, 3, 4]),
    pytest.param(dict(arr=[1, 2, 3, 4, 5], k=4, x=-1), [1, 2, 3, 4]),
])
def test_solutions(kwargs, expected):
    assert (Solution().findClosestElements(**kwargs)) == expected
    assert (SolutionMe().findClosestElements(**kwargs)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
