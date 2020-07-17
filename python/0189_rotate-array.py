#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:53:32
# @Last Modified : 2020-04-06 12:53:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#  说明:
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  要求使用空间复杂度为 O(1) 的 原地 算法。
#
#  Related Topics 数组
#  👍 627 👎 0

"""
from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        length = len(nums)
        k = k % length
        for i in range(k):
            v = nums.pop()
            nums.insert(0, v)

    def rotateReverse(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 2, 3, 4, 5, 6, 7]
    print(sol.rotateReverse(sample, 3))
    print(sample)
