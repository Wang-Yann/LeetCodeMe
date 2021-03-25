#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 12:19:52
# @Last Modified : 2020-04-05 12:19:52
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明:
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例:
#
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#  Related Topics 数组 双指针
#  👍 562 👎 0

"""

from typing import List

import pytest


class Solution00:

    def mergeArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:

        idx1, idx2 = 0, 0
        idx_total = 0
        ret = [0] * (m + n)
        while idx1 <= m - 1 and idx2 <= n - 1:
            if nums1[idx1] > nums2[idx2]:
                ret[idx_total] = nums2[idx2]
                idx2 += 1
            else:
                ret[idx_total] = nums1[idx1]
                idx1 += 1
            idx_total += 1
        while idx1 <= m - 1:
            ret[idx_total] = nums1[idx1]
            idx1 += 1
            idx_total += 1

        while idx2 <= n - 1:
            ret[idx_total] = nums2[idx2]
            idx2 += 1
            idx_total += 1
        return ret


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        idx_total = m + n - 1
        while idx_total >= 0 and idx2 >= 0 and idx1 >= 0:
            if nums2[idx2] >= nums1[idx1]:
                nums1[idx_total] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[idx_total] = nums1[idx1]
                idx1 -= 1
            idx_total -= 1
        # print("---", nums1, idx1, idx2, idx_total)
        while idx2 >= 0:
            nums1[idx_total] = nums2[idx2]
            idx_total -= 1
            idx2 -= 1


@pytest.mark.parametrize("kw,expected", [
    [dict(
        nums1=[1, 2, 3, 0, 0, 0], m=3,
        nums2=[2, 5, 6], n=3
    ), [1, 2, 2, 3, 5, 6]],
])
def test_solutions(kw, expected):
    assert Solution00().mergeArray(**kw) == expected
    Solution().merge(**kw)
    assert kw["nums1"] == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
