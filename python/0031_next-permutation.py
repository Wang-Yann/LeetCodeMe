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

from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = length - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def swap(self, nums: List[int], i: int, j: int) -> None:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums: List[int], start: int) -> None:
        left = start
        right = len(nums) - 1
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1


if __name__ == '__main__':
    sol = Solution()
    sample = [1, 5, 4, 3, 3, 2]
    sample = [1, 8, 7, 3, 5, 6]
    sample = [3, 2, 1]
    sample = [3, 2, 1, 4, 5, 2]
    # sample=[1,2,3]
    print(sol.nextPermutation(sample))
    print(sample)
