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


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 2:
            return []
        for i in range(0, length - 1):
            other = target - numbers[i]
            for j in range(i + 1, length):
                if numbers[j] == other:
                    return [i + 1, j + 1]
                elif   numbers[j]>other:
                    break
        return []

    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
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


if __name__ == '__main__':
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(numbers, target))
    print(sol.twoSum([2, 7, 9, 11, 15], 18))
    print(sol.twoSum([3, 2, 4], 6))
