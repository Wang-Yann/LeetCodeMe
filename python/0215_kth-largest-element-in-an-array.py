#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 11:39:12
# @Last Modified : 2020-04-28 11:39:12
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#  示例 1:
#
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
#  示例 2:
#
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
#  说明:
#
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#  Related Topics 堆 分治算法
#  👍 612 👎 0

"""
import heapq
import random
from typing import List

import pytest


class Solution0:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        res_list = heapq.nlargest(k, nums)
        return res_list[-1]


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            Hoare选择算法
            官方
            第 k 个最大元素也就是第 N - k 个最小元素
        """

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, k_smallest):
            """左闭右开"""
            if left == right:
                return nums[left]
            # select a random pivot_index between
            pivot_index = random.randint(left, right)
            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[3, 2, 1, 5, 6, 4], k=2), 5),
    pytest.param(dict(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4), 4),
])
def test_solutions(kwargs, expected):
    assert Solution0().findKthLargest(**kwargs) == expected
    assert Solution().findKthLargest(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
