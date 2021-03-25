#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 17:00:52
# @Last Modified : 2020-04-06 17:00:52
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
#  必须原地修改，只允许使用额外常数空间。
#
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#  Related Topics 数组
#  👍 574 👎 0

"""
import copy
from typing import List

import pytest


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        i = N - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = N - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, N - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


@pytest.mark.parametrize("args,expected", [
    ([1, 5, 4, 3, 3, 2], [2, 1, 3, 3, 4, 5]),
    ([1, 8, 7, 3, 5, 6], [1, 8, 7, 3, 6, 5]),
    ([3, 2, 1], [1, 2, 3]),
    ([3, 2, 1, 4, 5, 2], [3, 2, 1, 5, 2, 4]),
    ([4, 5, 2, 6, 3, 1], [4, 5, 3, 1, 2, 6]),
])
@pytest.mark.parametrize("SolutionCLS", [Solution])
def test_solutions(args, expected, SolutionCLS):
    arr = copy.deepcopy(args)
    SolutionCLS().nextPermutation(arr)
    assert arr == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
