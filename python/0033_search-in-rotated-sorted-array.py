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
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#  你可以假设数组中不存在重复的元素。
#
#  你的算法时间复杂度必须是 O(log n) 级别。
#
#  示例 1:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
#  示例 2:
#
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#  Related Topics 数组 二分查找
#  👍 829 👎 0

"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - right) // 2
            if nums[mid] == target:
                return mid
            elif (nums[left] <= target < nums[mid]) or (
                    nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1
        return -1


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        """思路更清晰"""
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    sample = [4, 5, 6, 7, 0, 1, 2]
    sample = [7, 9, 0, 1, 2, 3, 4, 5]
    print(sol.search(sample, 0))
