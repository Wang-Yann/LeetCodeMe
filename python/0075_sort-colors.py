#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 16:16:39
# @Last Modified : 2020-04-12 16:16:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
#  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
#  注意:
# 不能使用代码库中的排序函数来解决这道题。
#
#  示例:
#
#  输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
#
#  进阶：
#
#
#  一个直观的解决方案是使用计数排序的两趟扫描算法。
#  首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
#  你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#  Related Topics 排序 数组 双指针
#  👍 502 👎 0

"""

from typing import List

import pytest


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        三向切分
        """
        N = len(nums)
        lt, gt = 0, N - 1
        i = lt
        MID_V = 1
        while i <= gt:
            if nums[i] < MID_V:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
                i += 1
            elif nums[i] > MID_V:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1


@pytest.mark.parametrize("args,expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
])
def test_solutions(args, expected):
    Solution().sortColors(args)
    assert args == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
