#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20


"""
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
#  函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
#  说明:
#
#
#  返回的下标值（index1 和 index2）不是从零开始的。
#  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
#  示例:
#
#  输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#  Related Topics 数组 双指针 二分查找
#  👍 331 👎 0

"""

from typing import List

import pytest


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        二分
        """
        N = len(numbers)
        for i in range(N):
            low, high = i + 1, N - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]


class Solution1:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """双指针"""
        length = len(numbers)
        if length < 2:
            return []
        low = 0
        high = length - 1
        while low < high:
            sum_v = numbers[low] + numbers[high]
            if sum_v == target:
                return [low + 1, high + 1]
            elif sum_v < target:
                low += 1
            else:
                high -= 1
        return []


@pytest.mark.parametrize("args,expected", [
    ([[2, 7, 11, 15], 9], [1, 2]),
    ([[2, 7, 9, 11, 15], 18], [2, 4]),
])
def test_solutions(args, expected):
    assert Solution().twoSum(*args) == expected
    assert Solution1().twoSum(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
