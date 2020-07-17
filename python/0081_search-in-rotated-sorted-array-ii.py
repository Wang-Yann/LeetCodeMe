#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 17:41:24
# @Last Modified : 2020-04-06 17:41:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
#  编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
#  示例 1:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
#  示例 2:
#
#  输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
#  进阶:
#
#
#  这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。
#  这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#  Related Topics 数组 二分查找
#  👍 190 👎 0

"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+(right-right)//2
            if nums[mid]==target:
                return True
            elif (nums[left] <= target < nums[mid]) or (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right =mid-1
            else:
                left = mid+1
        return False


if __name__ == '__main__':
    sol = Solution()
    sample = [2,5,6,0,0,1,2]
    sample1 = [2,5,6,0,0,1,2]
    print(sol.search(sample, 0))
    print(sol.search(sample1, 3))
