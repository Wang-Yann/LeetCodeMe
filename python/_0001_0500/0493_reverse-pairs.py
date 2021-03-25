#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 22:56:37
# @Last Modified : 2020-04-30 22:56:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
#  你需要返回给定数组中的重要翻转对的数量。
#
#  示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
#  示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
#  注意:
#
#
#  给定数组的长度不会超过50000。
#  输入数组中的所有数字都在32位整数的表示范围内。
#
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法
#  👍 112 👎 0

"""

from typing import List

import pytest


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, start, mid, end):
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start + len(tmp)] = tmp

        def countAndMergeSort(nums, start, end):
            if end - start <= 0:
                return 0
            mid = (start + end) >> 1
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
            merge(nums, start, mid, end)
            return count

        return countAndMergeSort(nums, 0, len(nums) - 1)


@pytest.mark.parametrize("args,expected", [
    ([1, 3, 2, 3, 1], 2),
    pytest.param([2, 4, 3, 5, 1], 3),
])
def test_solutions(args, expected):
    assert Solution().reversePairs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
