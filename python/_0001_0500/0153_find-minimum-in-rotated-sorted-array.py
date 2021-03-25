#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 22:23:28
# @Last Modified : 2020-04-15 22:23:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  你可以假设数组中不存在重复元素。
#
#  示例 1:
#
#  输入: [3,4,5,1,2]
# 输出: 1
#
#  示例 2:
#
#  输入: [4,5,6,7,0,1,2]
# 输出: 0
#  Related Topics 数组 二分查找
#  👍 214 👎 0

"""

from typing import List

import pytest


class Solution:
    def findMinS(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        target = nums[-1]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                r = mid
            else:
                l = mid + 1
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:  # 循环不变式，如果left == right，则循环结束
            mid = (left + right) >> 1  # 地板除，mid更靠近left
            if nums[mid] > nums[right]:  # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:  # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid  # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        return nums[left]  # 循环结束，left == right，最小值输出nums[left]或nums[right]均可

    def findMin_Official(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1


@pytest.mark.parametrize("args,expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([1, 2], 1),
])
def test_solutions(args, expected):
    assert Solution().findMinS(args) == expected
    assert Solution().findMin(args) == expected
    assert Solution().findMin_Official(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
