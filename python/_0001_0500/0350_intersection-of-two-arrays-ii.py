#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 14:26:38
# @Last Modified : 2020-04-30 14:26:38
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

"""

import collections
from typing import List

import pytest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        it1, it2 = 0, 0
        while it1 <= len(nums1) - 1 and it2 <= len(nums2) - 1:
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res.append(nums1[it1])
                it1 += 1
                it2 += 1

        return res


class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums1) & collections.Counter(nums2)
        ans = []
        for i in c:
            ans.extend([i] * c[i])
        return ans


@pytest.mark.parametrize("kw,expected", [
    (dict(nums1=[1, 2, 2, 2, 1], nums2=[2, 2]), [2, 2]),
    (dict(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4]),
])
def test_solutions(kw, expected):
    assert sorted(Solution().intersect(**kw)) == sorted(expected)
    assert sorted(Solution1().intersect(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
